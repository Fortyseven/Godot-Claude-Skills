# Godot 4 C# Tutorials — Networking

> 6 tutorials. C#-specific code examples.

## High-level multiplayer

### High-level vs low-level API

The following explains the differences of high- and low-level networking in Godot as well as some fundamentals. If you want to jump in head-first and add networking to your first nodes, skip to **Initializing the network** below. But make sure to read the rest later on!

Godot always supported standard low-level networking via UDP, TCP and some higher-level protocols such as HTTP and SSL. These protocols are flexible and can be used for almost anything. However, using them to synchronize game state manually can be a large amount of work. Sometimes that work can't be avoided or is worth it, for example when working with a custom server implementation on the backend. But in most cases, it's worthwhile to consider Godot's high-level networking API, which sacrifices some of the fine-grained control of low-level networking for greater ease of use.

This is due to the inherent limitations of the low-level protocols:

- TCP ensures packets will always arrive reliably and in order, but latency is generally higher due to error correction. It's also quite a complex protocol because it understands what a "connection" is, and optimizes for goals that often don't suit applications like multiplayer games. Packets are buffered to be sent in larger batches, trading less per-packet overhead for higher latency. This can be useful for things like HTTP, but generally not for games. Some of this can be configured and disabled (e.g. by disabling "Nagle's algorithm" for the TCP connection).
- UDP is a simpler protocol, which only sends packets (and has no concept of a "connection"). No error correction makes it pretty quick (low latency), but packets may be lost along the way or received in the wrong order. Added to that, the MTU (maximum packet size) for UDP is generally low (only a few hundred bytes), so transmitting larger packets means splitting them, reorganizing them and retrying if a part fails.

In general, TCP can be thought of as reliable, ordered, and slow; UDP as unreliable, unordered and fast. Because of the large difference in performance, it often makes sense to re-build the parts of TCP wanted for games (optional reliability and packet order), while avoiding the unwanted parts (congestion/traffic control features, Nagle's algorithm, etc). Due to this, most game engines come with such an implementation, and Godot is no exception.

In summary, you can use the low-level networking API for maximum control and implement everything on top of bare network protocols or use the high-level API based on [SceneTree](../godot_csharp_core.md) that does most of the heavy lifting behind the scenes in a generally optimized way.

> **Note:** Most of Godot's supported platforms offer all or most of the mentioned high- and low-level networking features. As networking is always largely hardware and operating system dependent, however, some features may change or not be available on some target platforms. Most notably, the HTML5 platform currently offers WebSockets and WebRTC support but lacks some of the higher-level features, as well as raw access to low-level protocols like TCP and UDP.

> **Note:** More about TCP/IP, UDP, and networking: [https://gafferongames.com/post/udp_vs_tcp/](https://gafferongames.com/post/udp_vs_tcp/) Gaffer On Games has a lot of useful articles about networking in Games ([here](https://gafferongames.com/categories/game-networking/)), including the comprehensive [introduction to networking models in games](https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_networking/).

> **Warning:** Adding networking to your game comes with some responsibility. It can make your application vulnerable if done wrong and may lead to cheats or exploits. It may even allow an attacker to compromise the machines your application runs on and use your servers to send spam, attack others or steal your users' data if they play your game. This is always the case when networking is involved and has nothing to do with Godot. You can of course experiment, but when you release a networked application, always take care of any possible security concerns.

### Mid-level abstraction

Before going into how we would like to synchronize a game across the network, it can be helpful to understand how the base network API for synchronization works.

Godot uses a mid-level object [MultiplayerPeer](../godot_csharp_networking.md). This object is not meant to be created directly, but is designed so that several C++ implementations can provide it.

This object extends from [PacketPeer](../godot_csharp_networking.md), so it inherits all the useful methods for serializing, sending and receiving data. On top of that, it adds methods to set a peer, transfer mode, etc. It also includes signals that will let you know when peers connect or disconnect.

This class interface can abstract most types of network layers, topologies and libraries. By default, Godot provides an implementation based on ENet ([ENetMultiplayerPeer](../godot_csharp_networking.md)), one based on WebRTC ([WebRTCMultiplayerPeer](../godot_csharp_misc.md)), and one based on WebSocket ([WebSocketMultiplayerPeer](../godot_csharp_networking.md)), but this could be used to implement mobile APIs (for ad hoc WiFi, Bluetooth) or custom device/console-specific networking APIs.

For most common cases, using this object directly is discouraged, as Godot provides even higher level networking facilities. This object is still made available in case a game has specific needs for a lower-level API.

### Hosting considerations

When hosting a server, clients on your LAN can connect using the internal IP address which is usually of the form `192.168.*.*`. This internal IP address is **not** reachable by non-LAN/Internet clients.

On Windows, you can find your internal IP address by opening a command prompt and entering `ipconfig`. On macOS, open a Terminal and enter `ifconfig`. On Linux, open a terminal and enter `ip addr`.

If you're hosting a server on your own machine and want non-LAN clients to connect to it, you'll probably have to _forward_ the server port on your router. This is required to make your server reachable from the Internet since most residential connections use a [NAT](https://en.wikipedia.org/wiki/Network_address_translation). Godot's high-level multiplayer API only uses UDP, so you must forward the port in UDP, not just TCP.

After forwarding a UDP port and making sure your server uses that port, you can use [this website](https://icanhazip.com/) to find your public IP address. Then give this public IP address to any Internet clients that wish to connect to your server.

Godot's high-level multiplayer API uses a modified version of ENet which allows for full IPv6 support.

### Initializing the network

High-level networking in Godot is managed by the [SceneTree](../godot_csharp_core.md).

Each node has a `multiplayer` property, which is a reference to the `MultiplayerAPI` instance configured for it by the scene tree. Initially, every node is configured with the same default `MultiplayerAPI` object.

It is possible to create a new `MultiplayerAPI` object and assign it to a `NodePath` in the scene tree, which will override `multiplayer` for the node at that path and all of its descendants. This allows sibling nodes to be configured with different peers, which makes it possible to run a server and a client simultaneously in one instance of Godot.

```csharp
// By default, these expressions are interchangeable.
Multiplayer; // Get the MultiplayerAPI object configured for this node.
GetTree().GetMultiplayer(); // Get the default MultiplayerAPI object.
```

To initialize networking, a `MultiplayerPeer` object must be created, initialized as a server or client, and passed to the `MultiplayerAPI`.

```csharp
// Create client.
var peer = new ENetMultiplayerPeer();
peer.CreateClient(IPAddress, Port);
Multiplayer.MultiplayerPeer = peer;

// Create server.
var peer = new ENetMultiplayerPeer();
peer.CreateServer(Port, MaxClients);
Multiplayer.MultiplayerPeer = peer;
```

To terminate networking:

```csharp
Multiplayer.MultiplayerPeer = null;
```

> **Warning:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Managing connections

Every peer is assigned a unique ID. The server's ID is always 1, and clients are assigned a random positive integer.

Responding to connections or disconnections is possible by connecting to `MultiplayerAPI`'s signals:

- `peer_connected(id: int)` This signal is emitted with the newly connected peer's ID on each other peer, and on the new peer multiple times, once with each other peer's ID.
- `peer_disconnected(id: int)` This signal is emitted on every remaining peer when one disconnects.

The rest are only emitted on clients:

- `connected_to_server()`
- `connection_failed()`
- `server_disconnected()`

To get the unique ID of the associated peer:

```csharp
Multiplayer.GetUniqueId();
```

To check whether the peer is server or client:

```csharp
Multiplayer.IsServer();
```

### Remote procedure calls

Remote procedure calls, or RPCs, are functions that can be called on other peers. To create one, use the `@rpc` annotation before a function definition. To call an RPC, use `Callable`'s method `rpc()` to call in every peer, or `rpc_id()` to call in a specific peer.

```csharp
public override void _Ready()
{
    if (Multiplayer.IsServer())
    {
        Rpc(MethodName.PrintOncePerClient);
    }
}

[Rpc]
private void PrintOncePerClient()
{
    GD.Print("I will be printed to the console once per each connected client.");
}
```

RPCs will not serialize objects or callables.

For a remote call to be successful, the sending and receiving node need to have the same `NodePath`, which means they must have the same name. When using `add_child()` for nodes which are expected to use RPCs, set the argument `force_readable_name` to `true`.

> **Warning:** If a function is annotated with `@rpc` on the client script (resp. server script), then this function must also be declared on the server script (resp. client script). Both RPCs must have the same signature which is evaluated with a checksum of **all RPCs**. All RPCs in a script are checked at once, and all RPCs must be declared on both the client scripts and the server scripts, **even functions that are currently not in use**. The signature of the RPC includes the `@rpc()` declaration, the function, return type, **and** the NodePath. If an RPC resides in a script attached to `/root/Main/Node1`, then it must reside in precisely the same path and node on both the client script and the server script. Function arguments are not checked for matching between the server and client code (example: `func sendstuff():` and `func sendstuff(arg1, arg2):` **will pass** signature matching). If these conditions are not met (if all RPCs do not pass signature matching), the script may print an error or cause unwanted behavior. The error message may be unrelated to the RPC function you are currently building and testing. See further explanation and troubleshooting on [this post](https://github.com/godotengine/godot/issues/57869#issuecomment-1034215138).

The annotation can take a number of arguments, which have default values. `@rpc` is equivalent to:

```csharp
[Rpc(MultiplayerApi.RpcMode.Authority, CallLocal = false, TransferMode = MultiplayerPeer.TransferModeEnum.Reliable, TransferChannel = 0)]
```

The parameters and their functions are as follows:

`mode`:

- `"authority"`: Only the multiplayer authority can call remotely. The authority is the server by default, but can be changed per-node using [Node.set_multiplayer_authority](../godot_csharp_misc.md).
- `"any_peer"`: Clients are allowed to call remotely. Useful for transferring user input.

`sync`:

- `"call_remote"`: The function will not be called on the local peer.
- `"call_local"`: The function can be called on the local peer. Useful when the server is also a player.

`transfer_mode`:

- `"unreliable"` Packets are not acknowledged, can be lost, and can arrive at any order.
- `"unreliable_ordered"` Packets are received in the order they were sent in. This is achieved by ignoring packets that arrive later if another that was sent after them has already been received. Can cause packet loss if used incorrectly.
- `"reliable"` Resend attempts are sent until packets are acknowledged, and their order is preserved. Has a significant performance penalty.

`transfer_channel` is the channel index.

The first 3 can be passed in any order, but `transfer_channel` must always be last.

The function `multiplayer.get_remote_sender_id()` can be used to get the unique id of an rpc sender, when used within the function called by rpc.

```csharp
private void OnSomeInput() // Connected to some input.
{
    RpcId(1, MethodName.TransferSomeInput); // Send the input only to the server.
}

// Call local is required if the server is also a player.
[Rpc(MultiplayerApi.RpcMode.AnyPeer, CallLocal = true, TransferMode = MultiplayerPeer.TransferModeEnum.Reliable)]
private void TransferSomeInput()
{
    // The server knows who sent the input.
    int senderId = Multiplayer.GetRemoteSenderId();
    // Process the input and affect game logic.
}
```

### Channels

Modern networking protocols support channels, which are separate connections within the connection. This allows for multiple streams of packets that do not interfere with each other.

For example, game chat related messages and some of the core gameplay messages should all be sent reliably, but a gameplay message should not wait for a chat message to be acknowledged. This can be achieved by using different channels.

Channels are also useful when used with the unreliable ordered transfer mode. Sending packets of variable size with this transfer mode can cause packet loss, since packets which are slower to arrive are ignored. Separating them into multiple streams of homogeneous packets by using channels allows ordered transfer with little packet loss, and without the latency penalty caused by reliable mode.

The default channel with index 0 is actually three different channels - one for each transfer mode.

### Example lobby implementation

This is an example lobby that can handle peers joining and leaving, notify UI scenes through signals, and start the game after all clients have loaded the game scene.

```csharp
using Godot;

public partial class Lobby : Node
{
    public static Lobby Instance { get; private set; }

    // These signals can be connected to by a UI lobby scene or the game scene.
    [Signal]
    public delegate void PlayerConnectedEventHandler(int peerId, Godot.Collections.Dictionary<string, string> playerInfo);
    [Signal]
    public delegate void PlayerDisconnectedEventHandler(int peerId);
    [Signal]
    public delegate void ServerDisconnectedEventHandler();

    private const int Port = 7000;
    private const string DefaultServerIP = "127.0.0.1"; // IPv4 localhost
    private const int MaxConnections = 20;

    // This will contain player info for every player,
    // with the keys being each player's unique IDs.
    private Godot.Collections.Dictionary<long, Godot.Collectio
// ...
```

The game scene's root node should be named Game. In the script attached to it:

```csharp
using Godot;

public partial class Game : Node3D // Or Node2D.
{
    public override void _Ready()
    {
        // Preconfigure game.

        Lobby.Instance.RpcId(1, Lobby.MethodName.PlayerLoaded); // Tell the server that this peer has loaded.
    }

    // Called only on the server.
    public void StartGame()
    {
        // All peers are ready to receive RPCs in this scene.
    }
}
```

### Exporting for dedicated servers

Once you've made a multiplayer game, you may want to export it to run it on a dedicated server with no GPU available. See [Exporting for dedicated servers](tutorials_export.md) for more information.

> **Note:** The code samples on this page aren't designed to run on a dedicated server. You'll have to modify them so the server isn't considered to be a player. You'll also have to modify the game starting mechanism so that the first player who joins can start the game.

---

## HTTP client class

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

[HTTPClient](../godot_csharp_networking.md) provides low-level access to HTTP communication. For a higher-level interface, you may want to take a look at [HTTPRequest](../godot_csharp_networking.md) first, which has a tutorial available here.

> **Warning:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

Here's an example of using the [HTTPClient](../godot_csharp_networking.md) class. It's just a script, so it can be run by executing:

```csharp
c:\godot> godot -s HTTPTest.cs
```

It will connect and fetch a website.

```csharp
using Godot;

public partial class HTTPTest : SceneTree
{
    // HTTPClient demo.
    // This simple class can make HTTP requests; it will not block, but it needs to be polled.
    public override async void _Initialize()
    {
        Error err;
        HTTPClient http = new HTTPClient(); // Create the client.

        err = http.ConnectToHost("www.php.net", 80); // Connect to host/port.
        Debug.Assert(err == Error.Ok); // Make sure the connection is OK.

        // Wait until resolved and connected.
        while (http.GetStatus() == HTTPClient.Status.Connecting || http.GetStatus() == HTTPClient.Status.Resolving)
        {
            http.Poll();
            GD.Print("Connecting...");
            OS.DelayMsec(500);
        }

        Debug.Assert(http.GetStatus() == HTTPClient.Sta
// ...
```

---

## Making HTTP requests

### Why use HTTP?

[HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP) are useful to communicate with web servers and other non-Godot programs.

Compared to Godot's other networking features (like High-level multiplayer), HTTP requests have more overhead and take more time to get going, so they aren't suited for real-time communication, and aren't great to send lots of small updates as is common for multiplayer gameplay.

HTTP, however, offers interoperability with external web resources and is great at sending and receiving large amounts of data, for example to transfer files like game assets. These assets can then be loaded using [runtime file loading and saving](tutorials_io.md).

So HTTP may be useful for your game's login system, lobby browser, to retrieve some information from the web or to download game assets.

### HTTP requests in Godot

The [HTTPRequest](../godot_csharp_networking.md) node is the easiest way to make HTTP requests in Godot. It is backed by the more low-level [HTTPClient](../godot_csharp_networking.md), for which a tutorial is available here.

For this example, we will make an HTTP request to GitHub to retrieve the name of the latest Godot release.

> **Warning:** When exporting to **Android**, make sure to enable the **Internet** permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by the Android OS.

### Preparing the scene

Create a new empty scene, add a root [Node](../godot_csharp_core.md) and add a script to it. Then add an [HTTPRequest](../godot_csharp_networking.md) node as a child.

### Scripting the request

When the project is started (so in `_ready()`), we're going to send an HTTP request to Github using our [HTTPRequest](../godot_csharp_networking.md) node, and once the request completes, we're going to parse the returned JSON data, look for the `name` field and print that to console.

```csharp
using Godot;
using System.Text;

public partial class MyNode : Node
{
    public override void _Ready()
    {
        HttpRequest httpRequest = GetNode<HttpRequest>("HTTPRequest");
        httpRequest.RequestCompleted += OnRequestCompleted;
        httpRequest.Request("https://api.github.com/repos/godotengine/godot/releases/latest");
    }

    private void OnRequestCompleted(long result, long responseCode, string[] headers, byte[] body)
    {
        Godot.Collections.Dictionary json = Json.ParseString(Encoding.UTF8.GetString(body)).AsGodotDictionary();
        GD.Print(json["name"]);
    }
}
```

Save the script and the scene, and run the project. The name of the most recent Godot release on Github should be printed to the output log. For more information on parsing JSON, see the class references for [JSON](../godot_csharp_filesystem.md).

Note that you may want to check whether the `result` equals `RESULT_SUCCESS` and whether a JSON parsing error occurred, see the JSON class reference and [HTTPRequest](../godot_csharp_networking.md) for more.

You have to wait for a request to finish before sending another one. Making multiple request at once requires you to have one node per request. A common strategy is to create and delete HTTPRequest nodes at runtime as necessary.

### Sending data to the server

Until now, we have limited ourselves to requesting data from a server. But what if you need to send data to the server? Here is a common way of doing it:

```csharp
string json = Json.Stringify(dataToSend);
string[] headers = ["Content-Type: application/json"];
HttpRequest httpRequest = GetNode<HttpRequest>("HTTPRequest");
httpRequest.Request(url, headers, HttpClient.Method.Post, json);
```

### Setting custom HTTP headers

Of course, you can also set custom HTTP headers. These are given as a string array, with each string containing a header in the format `"header: value"`. For example, to set a custom user agent (the HTTP `User-Agent` header) you could use the following:

```csharp
HttpRequest httpRequest = GetNode<HttpRequest>("HTTPRequest");
httpRequest.Request("https://api.github.com/repos/godotengine/godot/releases/latest", ["User-Agent: YourCustomUserAgent"]);
```

> **Danger:** Be aware that someone might analyse and decompile your released application and thus may gain access to any embedded authorization information like tokens, usernames or passwords. That means it is usually not a good idea to embed things such as database access credentials inside your game. Avoid providing information useful to an attacker whenever possible.

---

## TLS/SSL certificates

### Introduction

It is often desired to use TLS connections (also known as SSL connections) for communications to avoid "man in the middle" attacks. Godot has a connection wrapper, [StreamPeerTLS](../godot_csharp_networking.md), which can take a regular connection and add security around it. The [HTTPClient](../godot_csharp_networking.md) and [HTTPRequest](../godot_csharp_networking.md) classes also support HTTPS using this same wrapper.

Godot will try to use the TLS certificate bundle provided by the operating system, but also includes the [TLS certificate bundle from Mozilla](https://github.com/godotengine/godot/blob/master/thirdparty/certs/ca-certificates.crt) as a fallback.

You can alternatively force your own certificate bundle in the Project Settings:

When set, this file _overrides_ the operating system provided bundle by default. This file should contain any number of public certificates in [PEM format](https://en.wikipedia.org/wiki/Privacy-enhanced_Electronic_Mail).

There are two ways to obtain certificates:

### Obtain a certificate from a certificate authority

The main approach to getting a certificate is to use a certificate authority (CA) such as [Let's Encrypt](https://letsencrypt.org/). This is a more cumbersome process than a self-signed certificate, but it's more "official" and ensures your identity is clearly represented. The resulting certificate is also trusted by applications such as web browsers, unlike a self-signed certificate which requires additional configuration on the client side before it's considered trusted.

These certificates do not require any configuration on the client to work, since Godot already bundles the Mozilla certificate bundle in the editor and exported projects.

### Generate a self-signed certificate

For most use cases, it's recommended to go through certificate authority as the process is free with certificate authorities such as Let's Encrypt. However, if using a certificate authority is not an option, then you can generate a self-signed certificate and tell the client to consider your self-signed certificate as trusted.

To create a self-signed certificate, generate a private and public key pair and add the public key (in PEM format) to the CRT file specified in the Project Settings.

> **Warning:** The private key should **only** go to your server. The client must not have access to it: otherwise, the security of the certificate will be compromised.

> **Warning:** When specifying a self-signed certificate as TLS bundle in the project settings, normal domain name validation is enforced via the certificate CN and alternative names. See [TLSOptions](../godot_csharp_networking.md) to customize domain name validation.

For development purposes Godot can generate self-signed certificates via [Crypto.generate_self_signed_certificate](../godot_csharp_networking.md).

Alternatively, OpenSSL has some documentation about [generating keys](https://raw.githubusercontent.com/openssl/openssl/master/doc/HOWTO/keys.txt) and [certificates](https://raw.githubusercontent.com/openssl/openssl/master/doc/HOWTO/certificates.txt).

---

## WebRTC

> **Work in progress:** The content of this page was not yet updated for Godot `4.6` and may be **outdated**. If you know how to improve this page or you can confirm that it's up to date, feel free to [open a pull request](https://github.com/godotengine/godot-docs).

### HTML5, WebSocket, WebRTC

One of Godot's great features is its ability to export to the HTML5/WebAssembly platform, allowing your game to run directly in the browser when a user visit your webpage.

This is a great opportunity for both demos and full games, but used to come with some limitations. In the area of networking, browsers used to support only HTTPRequests until recently, when first WebSocket and then WebRTC were proposed as standards.

#### WebSocket

When the WebSocket protocol was standardized in December 2011, it allowed browsers to create stable and bidirectional connections to a WebSocket server. The protocol is a very powerful tool to send push notifications to browsers, and has been used to implement chats, turn-based games, etc.

WebSockets, though, still use a TCP connection, which is good for reliability but not for latency, so not good for real-time applications like VoIP and fast-paced games.

#### WebRTC

For this reason, since 2010, Google started working on a new technology called WebRTC, which later on, in 2017, became a W3C candidate recommendation. WebRTC is a much more complex set of specifications, and relies on many other technologies behind the scenes (ICE, DTLS, SDP) to provide fast, real-time, and secure communication between two peers.

The idea is to find the fastest route between the two peers and establish whenever possible a direct communication (i.e. try to avoid a relaying server).

However, this comes at a price, which is that some media information must be exchanged between the two peers before the communication can start (in the form of Session Description Protocol - SDP strings). This usually takes the form of a so-called WebRTC Signaling Server.

Peers connect to a signaling server (for example a WebSocket server) and send their media information. The server then relays this information to other peers, allowing them to establish the desired direct communication. Once this step is done, peers can disconnect from the signaling server and keep the direct Peer-to-Peer (P2P) connection open.

### Using WebRTC in Godot

WebRTC is implemented in Godot via two main classes [WebRTCPeerConnection](../godot_csharp_misc.md) and [WebRTCDataChannel](../godot_csharp_misc.md), plus the multiplayer API implementation [WebRTCMultiplayerPeer](../godot_csharp_misc.md). See section on high-level multiplayer for more details.

> **Note:** These classes are available automatically in HTML5, but **require an external GDExtension plugin on native (non-HTML5) platforms**. Check out the [webrtc-native plugin repository](https://github.com/godotengine/webrtc-native) for instructions and to get the latest [release](https://github.com/godotengine/webrtc-native/releases).

> **Warning:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

#### Minimal connection example

This example will show you how to create a WebRTC connection between two peers in the same application. This is not very useful in real life, but will give you a good overview of how a WebRTC connection is set up.

This will print:

#### Local signaling example

This example expands on the previous one, separating the peers in two different scenes, and using a [singleton](tutorials_scripting.md) as a signaling server.

And now for the local signaling server:

> **Note:** This local signaling server is supposed to be used as a [singleton](tutorials_scripting.md) to connect two peers in the same scene.

Then you can use it like this:

This will print something similar to this:

#### Remote signaling with WebSocket

A more advanced demo using WebSocket for signaling peers and [WebRTCMultiplayerPeer](../godot_csharp_misc.md) is available in the [godot demo projects](https://github.com/godotengine/godot-demo-projects) under networking/webrtc_signaling.

---

## Using WebSockets

### HTML5 and WebSocket

The WebSocket protocol was standardized in 2011 with the original goal of allowing browsers to create stable and bidirectional connections with a server. Before that, browsers used to only support HTTP requests, which aren't well-suited for bidirectional communication.

The protocol is message-based and a very powerful tool to send push notifications to browsers. It has been used to implement chats, turn-based games, and more. It still uses a TCP connection, which is good for reliability but not for latency, so it's not good for real-time applications like VoIP and fast-paced games (see WebRTC for those use cases).

Due to its simplicity, its wide compatibility, and being easier to use than a raw TCP connection, WebSocket started to spread outside the browsers, in native applications as a mean to communicate with network servers.

Godot supports WebSocket in both native and web exports.

### Using WebSocket in Godot

WebSocket is implemented in Godot via [WebSocketPeer](../godot_csharp_networking.md). The WebSocket implementation is compatible with the High-Level Multiplayer. See section on high-level multiplayer for more details.

> **Warning:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

#### Minimal client example

This example will show you how to create a WebSocket connection to a remote server, and how to send and receive data.

This will print something similar to:

```text
Connecting to wss://echo.websocket.org...
< Got text data from server: Request served by 7811941c69e658
> Sending test packet.
< Got text data from server: Test packet
```

#### Minimal server example

This example will show you how to create a WebSocket server that listens for remote connections, and how to send and receive data.

When a client connects, this will print something similar to this:

```text
Server started.
+ Peer 2 connected.
< Got text data from peer 2: Test packet ... echoing
```

#### Advanced chat demo

A more advanced chat demo which optionally uses the multiplayer mid-level abstraction and a high-level multiplayer demo are available in the [godot demo projects](https://github.com/godotengine/godot-demo-projects) under networking/websocket_chat and networking/websocket_multiplayer.

---
