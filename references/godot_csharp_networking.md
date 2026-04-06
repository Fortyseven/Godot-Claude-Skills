# Godot 4 C# API Reference — Networking

> C#-only reference. 34 classes.

### AESContext
*Inherits: **RefCounted < Object***

This class holds the context information required for encryption and decryption operations with AES (Advanced Encryption Standard). Both AES-ECB and AES-CBC modes are supported.

**Methods**
- `void Finish()`
- `PackedByteArray GetIvState()`
- `Error Start(Mode mode, PackedByteArray key, PackedByteArray iv = PackedByteArray())`
- `PackedByteArray Update(PackedByteArray src)`

**C# Examples**
```csharp
using Godot;
using System.Diagnostics;

public partial class MyNode : Node
{
    private AesContext _aes = new AesContext();

    public override void _Ready()
    {
        string key = "My secret key!!!"; // Key must be either 16 or 32 bytes.
        string data = "My secret text!!"; // Data size must be multiple of 16 bytes, apply padding if needed.
        // Encrypt ECB
        _aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer());
        byte[] encrypted = _aes.Update(data.ToUtf8Buffer());
        _aes.Finish();
        // Decrypt ECB
        _aes.Start(AesContext.Mode.EcbDecrypt,
// ...
```

### CryptoKey
*Inherits: **Resource < RefCounted < Object***

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any other Resource.

**Methods**
- `bool IsPublicOnly()`
- `Error Load(string path, bool publicOnly = false)`
- `Error LoadFromString(string stringKey, bool publicOnly = false)`
- `Error Save(string path, bool publicOnly = false)`
- `string SaveToString(bool publicOnly = false)`

### Crypto
*Inherits: **RefCounted < Object***

The Crypto class provides access to advanced cryptographic functionalities.

**Methods**
- `bool ConstantTimeCompare(PackedByteArray trusted, PackedByteArray received)`
- `PackedByteArray Decrypt(CryptoKey key, PackedByteArray ciphertext)`
- `PackedByteArray Encrypt(CryptoKey key, PackedByteArray plaintext)`
- `PackedByteArray GenerateRandomBytes(int size)`
- `CryptoKey GenerateRsa(int size)`
- `X509Certificate GenerateSelfSignedCertificate(CryptoKey key, string issuerName = "CN=myserver, Variant O = myorganisation, Variant C = IT", string notBefore = "20140101000000", string notAfter = "20340101000000")`
- `PackedByteArray HmacDigest(HashType hashType, PackedByteArray key, PackedByteArray msg)`
- `PackedByteArray Sign(HashType hashType, PackedByteArray hash, CryptoKey key)`
- `bool Verify(HashType hashType, PackedByteArray hash, PackedByteArray signature, CryptoKey key)`

**C# Examples**
```csharp
using Godot;
using System.Diagnostics;

Crypto crypto = new Crypto();

// Generate new RSA key.
CryptoKey key = crypto.GenerateRsa(4096);

// Generate new self-signed certificate with the given key.
X509Certificate cert = crypto.GenerateSelfSignedCertificate(key, "CN=mydomain.com,O=My Game Company,C=IT");

// Save key and certificate in the user folder.
key.Save("user://generated.key");
cert.Save("user://generated.crt");

// Encryption
string data = "Some data";
byte[] encrypted = crypto.Encrypt(key, data.ToUtf8Buffer());

// Decryption
byte[] decrypted = crypto.Decrypt(key, encrypted);

// Si
// ...
```
```csharp
var crypto = new Crypto();
// Generate 4096 bits RSA key.
CryptoKey key = crypto.GenerateRsa(4096);
// Generate self-signed certificate using the given key.
X509Certificate cert = crypto.GenerateSelfSignedCertificate(key, "CN=mydomain.com,O=My Game Company,C=IT");
```

### DTLSServer
*Inherits: **RefCounted < Object***

This class is used to store the state of a DTLS server. Upon setup() it converts connected PacketPeerUDP to PacketPeerDTLS accepting them via take_connection() as DTLS clients. Under the hood, this class is used to store the DTLS state and cookies of the server. The reason of why the state and cookies are needed is outside of the scope of this documentation.

**Methods**
- `Error Setup(TLSOptions serverOptions)`
- `PacketPeerDTLS TakeConnection(PacketPeerUDP udpPeer)`

**C# Examples**
```csharp
// ServerNode.cs
using Godot;

public partial class ServerNode : Node
{
    private DtlsServer _dtls = new DtlsServer();
    private UdpServer _server = new UdpServer();
    private Godot.Collections.Array<PacketPeerDtls> _peers = [];

    public override void _Ready()
    {
        _server.Listen(4242);
        var key = GD.Load<CryptoKey>("key.key"); // Your private key.
        var cert = GD.Load<X509Certificate>("cert.crt"); // Your X509 certificate.
        _dtls.Setup(TlsOptions.Server(key, cert));
    }

    public override void _Process(double delta)
    {
        while (_server.IsConn
// ...
```
```csharp
// ClientNode.cs
using Godot;
using System.Text;

public partial class ClientNode : Node
{
    private PacketPeerDtls _dtls = new PacketPeerDtls();
    private PacketPeerUdp _udp = new PacketPeerUdp();
    private bool _connected = false;

    public override void _Ready()
    {
        _udp.ConnectToHost("127.0.0.1", 4242);
        _dtls.ConnectToPeer(_udp, validateCerts: false); // Use true in production for certificate validation!
    }

    public override void _Process(double delta)
    {
        _dtls.Poll();
        if (_dtls.GetStatus() == PacketPeerDtls.Status.Connected)
        {

// ...
```

### ENetConnection
*Inherits: **RefCounted < Object***

ENet's purpose is to provide a relatively thin, simple and robust network communication layer on top of UDP (User Datagram Protocol).

**Methods**
- `void BandwidthLimit(int inBandwidth = 0, int outBandwidth = 0)`
- `void Broadcast(int channel, PackedByteArray packet, int flags)`
- `void ChannelLimit(int limit)`
- `void Compress(CompressionMode mode)`
- `ENetPacketPeer ConnectToHost(string address, int port, int channels = 0, int data = 0)`
- `Error CreateHost(int maxPeers = 32, int maxChannels = 0, int inBandwidth = 0, int outBandwidth = 0)`
- `Error CreateHostBound(string bindAddress, int bindPort, int maxPeers = 32, int maxChannels = 0, int inBandwidth = 0, int outBandwidth = 0)`
- `void Destroy()`
- `Error DtlsClientSetup(string hostname, TLSOptions clientOptions = null)`
- `Error DtlsServerSetup(TLSOptions serverOptions)`
- `void Flush()`
- `int GetLocalPort()`
- `int GetMaxChannels()`
- `Array[ENetPacketPeer] GetPeers()`
- `float PopStatistic(HostStatistic statistic)`
- `void RefuseNewConnections(bool refuse)`
- `Godot.Collections.Array Service(int timeout = 0)`
- `void SocketSend(string destinationAddress, int destinationPort, PackedByteArray packet)`

### ENetMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

A MultiplayerPeer implementation that should be passed to MultiplayerAPI.multiplayer_peer after being initialized as either a client, server, or mesh. Events can then be handled by connecting to MultiplayerAPI signals. See ENetConnection for more information on the ENet library wrapper.

**Properties**
- `ENetConnection Host`

**Methods**
- `Error AddMeshPeer(int peerId, ENetConnection host)`
- `Error CreateClient(string address, int port, int channelCount = 0, int inBandwidth = 0, int outBandwidth = 0, int localPort = 0)`
- `Error CreateMesh(int uniqueId)`
- `Error CreateServer(int port, int maxClients = 32, int maxChannels = 0, int inBandwidth = 0, int outBandwidth = 0)`
- `ENetPacketPeer GetPeer(int id)`
- `void SetBindIp(string ip)`

### ENetPacketPeer
*Inherits: **PacketPeer < RefCounted < Object***

A PacketPeer implementation representing a peer of an ENetConnection.

**Methods**
- `int GetChannels()`
- `int GetPacketFlags()`
- `string GetRemoteAddress()`
- `int GetRemotePort()`
- `PeerState GetState()`
- `float GetStatistic(PeerStatistic statistic)`
- `bool IsActive()`
- `void PeerDisconnect(int data = 0)`
- `void PeerDisconnectLater(int data = 0)`
- `void PeerDisconnectNow(int data = 0)`
- `void Ping()`
- `void PingInterval(int pingInterval)`
- `void Reset()`
- `Error Send(int channel, PackedByteArray packet, int flags)`
- `void SetTimeout(int timeout, int timeoutMin, int timeoutMax)`
- `void ThrottleConfigure(int interval, int acceleration, int deceleration)`

### HTTPClient
*Inherits: **RefCounted < Object***

Hyper-text transfer protocol client (sometimes called "User Agent"). Used to make HTTP requests to download web content, upload files and other data or to communicate with various services, among other use cases.

**Properties**
- `bool BlockingModeEnabled` = `false`
- `StreamPeer Connection`
- `int ReadChunkSize` = `65536`

**Methods**
- `void Close()`
- `Error ConnectToHost(string host, int port = -1, TLSOptions tlsOptions = null)`
- `int GetResponseBodyLength()`
- `int GetResponseCode()`
- `PackedStringArray GetResponseHeaders()`
- `Godot.Collections.Dictionary GetResponseHeadersAsDictionary()`
- `Status GetStatus()`
- `bool HasResponse()`
- `bool IsResponseChunked()`
- `Error Poll()`
- `string QueryStringFromDict(Godot.Collections.Dictionary fields)`
- `PackedByteArray ReadResponseBodyChunk()`
- `Error Request(Method method, string url, PackedStringArray headers, string body = "")`
- `Error RequestRaw(Method method, string url, PackedStringArray headers, PackedByteArray body)`
- `void SetHttpProxy(string host, int port)`
- `void SetHttpsProxy(string host, int port)`

**C# Examples**
```csharp
var fields = new Godot.Collections.Dictionary { { "username", "user" }, { "password", "pass" } };
string queryString = httpClient.QueryStringFromDict(fields);
// Returns "username=user&password=pass"
```
```csharp
var fields = new Godot.Collections.Dictionary
{
    { "single", 123 },
    { "notValued", default },
    { "multiple", new Godot.Collections.Array { 22, 33, 44 } },
};
string queryString = httpClient.QueryStringFromDict(fields);
// Returns "single=123&not_valued&multiple=22&multiple=33&multiple=44"
```

### HTTPRequest
*Inherits: **Node < Object***

A node with the ability to send HTTP requests. Uses HTTPClient internally.

**Properties**
- `bool AcceptGzip` = `true`
- `int BodySizeLimit` = `-1`
- `int DownloadChunkSize` = `65536`
- `string DownloadFile` = `""`
- `int MaxRedirects` = `8`
- `float Timeout` = `0.0`
- `bool UseThreads` = `false`

**Methods**
- `void CancelRequest()`
- `int GetBodySize()`
- `int GetDownloadedBytes()`
- `Status GetHttpClientStatus()`
- `Error Request(string url, PackedStringArray customHeaders = PackedStringArray(), Method method = 0, string requestData = "")`
- `Error RequestRaw(string url, PackedStringArray customHeaders = PackedStringArray(), Method method = 0, PackedByteArray requestDataRaw = PackedByteArray())`
- `void SetHttpProxy(string host, int port)`
- `void SetHttpsProxy(string host, int port)`
- `void SetTlsOptions(TLSOptions clientOptions)`

**C# Examples**
```csharp
public override void _Ready()
{
    // Create an HTTP request node and connect its completion signal.
    var httpRequest = new HttpRequest();
    AddChild(httpRequest);
    httpRequest.RequestCompleted += HttpRequestCompleted;

    // Perform a GET request. The URL below returns JSON as of writing.
    Error error = httpRequest.Request("https://httpbin.org/get");
    if (error != Error.Ok)
    {
        GD.PushError("An error occurred in the HTTP request.");
    }

    // Perform a POST request. The URL below returns JSON as of writing.
    // Note: Don't make simultaneous requests using a si
// ...
```
```csharp
public override void _Ready()
{
    // Create an HTTP request node and connect its completion signal.
    var httpRequest = new HttpRequest();
    AddChild(httpRequest);
    httpRequest.RequestCompleted += HttpRequestCompleted;

    // Perform the HTTP request. The URL below returns a PNG image as of writing.
    Error error = httpRequest.Request("https://placehold.co/512.png");
    if (error != Error.Ok)
    {
        GD.PushError("An error occurred in the HTTP request.");
    }
}

// Called when the HTTP request is completed.
private void HttpRequestCompleted(long result, long responseCode,
// ...
```

### HashingContext
*Inherits: **RefCounted < Object***

The HashingContext class provides an interface for computing cryptographic hashes over multiple iterations. Useful for computing hashes of big files (so you don't have to load them all in memory), network streams, and data streams in general (so you don't have to hold buffers).

**Methods**
- `PackedByteArray Finish()`
- `Error Start(HashType type)`
- `Error Update(PackedByteArray chunk)`

**C# Examples**
```csharp
public const int ChunkSize = 1024;

public void HashFile(string path)
{
    // Check that file exists.
    if (!FileAccess.FileExists(path))
    {
        return;
    }
    // Start an SHA-256 context.
    var ctx = new HashingContext();
    ctx.Start(HashingContext.HashType.Sha256);
    // Open the file to hash.
    using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
    // Update the context after reading each chunk.
    while (file.GetPosition() < file.GetLength())
    {
        int remaining = (int)(file.GetLength() - file.GetPosition());
        ctx.Update(file.GetBuffer(Ma
// ...
```

### MultiplayerAPIExtension
*Inherits: **MultiplayerAPI < RefCounted < Object***

This class can be used to extend or replace the default MultiplayerAPI implementation via script or extensions.

**Methods**
- `MultiplayerPeer _GetMultiplayerPeer() [virtual]`
- `PackedInt32Array _GetPeerIds() [virtual]`
- `int _GetRemoteSenderId() [virtual]`
- `int _GetUniqueId() [virtual]`
- `Error _ObjectConfigurationAdd(Object object, Variant configuration) [virtual]`
- `Error _ObjectConfigurationRemove(Object object, Variant configuration) [virtual]`
- `Error _Poll() [virtual]`
- `Error _Rpc(int peer, Object object, StringName method, Godot.Collections.Array args) [virtual]`
- `void _SetMultiplayerPeer(MultiplayerPeer multiplayerPeer) [virtual]`

### MultiplayerAPI
*Inherits: **RefCounted < Object** | Inherited by: MultiplayerAPIExtension, SceneMultiplayer*

Base class for high-level multiplayer API implementations. See also MultiplayerPeer.

**Properties**
- `MultiplayerPeer MultiplayerPeer`

**Methods**
- `MultiplayerAPI CreateDefaultInterface() [static]`
- `StringName GetDefaultInterface() [static]`
- `PackedInt32Array GetPeers()`
- `int GetRemoteSenderId()`
- `int GetUniqueId()`
- `bool HasMultiplayerPeer()`
- `bool IsServer()`
- `Error ObjectConfigurationAdd(Object object, Variant configuration)`
- `Error ObjectConfigurationRemove(Object object, Variant configuration)`
- `Error Poll()`
- `Error Rpc(int peer, Object object, StringName method, Godot.Collections.Array arguments = [])`
- `void SetDefaultInterface(StringName interfaceName) [static]`

### MultiplayerPeerExtension
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods below must be implemented to have a working custom multiplayer implementation. See also MultiplayerAPI.

**Methods**
- `void _Close() [virtual]`
- `void _DisconnectPeer(int pPeer, bool pForce) [virtual]`
- `int _GetAvailablePacketCount() [virtual]`
- `ConnectionStatus _GetConnectionStatus() [virtual]`
- `int _GetMaxPacketSize() [virtual]`
- `Error _GetPacket(const uint8_t ** rBuffer, int32_t* rBufferSize) [virtual]`
- `int _GetPacketChannel() [virtual]`
- `TransferMode _GetPacketMode() [virtual]`
- `int _GetPacketPeer() [virtual]`
- `PackedByteArray _GetPacketScript() [virtual]`
- `int _GetTransferChannel() [virtual]`
- `TransferMode _GetTransferMode() [virtual]`
- `int _GetUniqueId() [virtual]`
- `bool _IsRefusingNewConnections() [virtual]`
- `bool _IsServer() [virtual]`
- `bool _IsServerRelaySupported() [virtual]`
- `void _Poll() [virtual]`
- `Error _PutPacket(const uint8_t* pBuffer, int pBufferSize) [virtual]`
- `Error _PutPacketScript(PackedByteArray pBuffer) [virtual]`
- `void _SetRefuseNewConnections(bool pEnable) [virtual]`
- `void _SetTargetPeer(int pPeer) [virtual]`
- `void _SetTransferChannel(int pChannel) [virtual]`
- `void _SetTransferMode(TransferMode pMode) [virtual]`

### MultiplayerPeer
*Inherits: **PacketPeer < RefCounted < Object** | Inherited by: ENetMultiplayerPeer, MultiplayerPeerExtension, OfflineMultiplayerPeer, WebRTCMultiplayerPeer, WebSocketMultiplayerPeer*

Manages the connection with one or more remote peers acting as server or client and assigning unique IDs to each of them. See also MultiplayerAPI.

**Properties**
- `bool RefuseNewConnections` = `false`
- `int TransferChannel` = `0`
- `TransferMode TransferMode` = `2`

**Methods**
- `void Close()`
- `void DisconnectPeer(int peer, bool force = false)`
- `int GenerateUniqueId()`
- `ConnectionStatus GetConnectionStatus()`
- `int GetPacketChannel()`
- `TransferMode GetPacketMode()`
- `int GetPacketPeer()`
- `int GetUniqueId()`
- `bool IsServerRelaySupported()`
- `void Poll()`
- `void SetTargetPeer(int id)`

### PacketPeerDTLS
*Inherits: **PacketPeer < RefCounted < Object***

This class represents a DTLS peer connection. It can be used to connect to a DTLS server, and is returned by DTLSServer.take_connection().

**Methods**
- `Error ConnectToPeer(PacketPeerUDP packetPeer, string hostname, TLSOptions clientOptions = null)`
- `void DisconnectFromPeer()`
- `Status GetStatus()`
- `void Poll()`

### PacketPeerExtension
*Inherits: **PacketPeer < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `int _GetAvailablePacketCount() [virtual]`
- `int _GetMaxPacketSize() [virtual]`
- `Error _GetPacket(const uint8_t ** rBuffer, int32_t* rBufferSize) [virtual]`
- `Error _PutPacket(const uint8_t* pBuffer, int pBufferSize) [virtual]`

### PacketPeerStream
*Inherits: **PacketPeer < RefCounted < Object***

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

**Properties**
- `int InputBufferMaxSize` = `65532`
- `int OutputBufferMaxSize` = `65532`
- `StreamPeer StreamPeer`

### PacketPeerUDP
*Inherits: **PacketPeer < RefCounted < Object***

UDP packet peer. Can be used to send and receive raw UDP packets as well as Variants.

**Methods**
- `Error Bind(int port, string bindAddress = "*", int recvBufSize = 65536)`
- `void Close()`
- `Error ConnectToHost(string host, int port)`
- `int GetLocalPort()`
- `string GetPacketIp()`
- `int GetPacketPort()`
- `bool IsBound()`
- `bool IsSocketConnected()`
- `Error JoinMulticastGroup(string multicastAddress, string interfaceName)`
- `Error LeaveMulticastGroup(string multicastAddress, string interfaceName)`
- `void SetBroadcastEnabled(bool enabled)`
- `Error SetDestAddress(string host, int port)`
- `Error Wait()`

**C# Examples**
```csharp
var socket = new PacketPeerUdp();
// Server
socket.SetDestAddress("127.0.0.1", 789);
socket.PutPacket("Time to stop".ToAsciiBuffer());

// Client
while (socket.Wait() == OK)
{
    string data = socket.GetPacket().GetStringFromASCII();
    if (data == "Time to stop")
    {
        return;
    }
}
```

### PacketPeer
*Inherits: **RefCounted < Object** | Inherited by: ENetPacketPeer, MultiplayerPeer, PacketPeerDTLS, PacketPeerExtension, PacketPeerStream, PacketPeerUDP, ...*

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low-level bytes or having to worry about network ordering.

**Properties**
- `int EncodeBufferMaxSize` = `8388608`

**Methods**
- `int GetAvailablePacketCount()`
- `PackedByteArray GetPacket()`
- `Error GetPacketError()`
- `Variant GetVar(bool allowObjects = false)`
- `Error PutPacket(PackedByteArray buffer)`
- `Error PutVar(Variant var, bool fullObjects = false)`

### SceneMultiplayer
*Inherits: **MultiplayerAPI < RefCounted < Object***

This class is the default implementation of MultiplayerAPI, used to provide multiplayer functionalities in Godot Engine.

**Properties**
- `bool AllowObjectDecoding` = `false`
- `Callable AuthCallback` = `Callable()`
- `float AuthTimeout` = `3.0`
- `int MaxDeltaPacketSize` = `65535`
- `int MaxSyncPacketSize` = `1350`
- `bool RefuseNewConnections` = `false`
- `NodePath RootPath` = `NodePath("")`
- `bool ServerRelay` = `true`

**Methods**
- `void Clear()`
- `Error CompleteAuth(int id)`
- `void DisconnectPeer(int id)`
- `PackedInt32Array GetAuthenticatingPeers()`
- `Error SendAuth(int id, PackedByteArray data)`
- `Error SendBytes(PackedByteArray bytes, int id = 0, TransferMode mode = 2, int channel = 0)`

### StreamPeerBuffer
*Inherits: **StreamPeer < RefCounted < Object***

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, FileAccess can be used directly.

**Properties**
- `PackedByteArray DataArray` = `PackedByteArray()`

**Methods**
- `void Clear()`
- `StreamPeerBuffer Duplicate()`
- `int GetPosition()`
- `int GetSize()`
- `void Resize(int size)`
- `void Seek(int position)`

### StreamPeerExtension
*Inherits: **StreamPeer < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `int _GetAvailableBytes() [virtual]`
- `Error _GetData(uint8_t* rBuffer, int rBytes, int32_t* rReceived) [virtual]`
- `Error _GetPartialData(uint8_t* rBuffer, int rBytes, int32_t* rReceived) [virtual]`
- `Error _PutData(const uint8_t* pData, int pBytes, int32_t* rSent) [virtual]`
- `Error _PutPartialData(const uint8_t* pData, int pBytes, int32_t* rSent) [virtual]`

### StreamPeerGZIP
*Inherits: **StreamPeer < RefCounted < Object***

This class allows to compress or decompress data using GZIP/deflate in a streaming fashion. This is particularly useful when compressing or decompressing files that have to be sent through the network without needing to allocate them all in memory.

**Methods**
- `void Clear()`
- `Error Finish()`
- `Error StartCompression(bool useDeflate = false, int bufferSize = 65535)`
- `Error StartDecompression(bool useDeflate = false, int bufferSize = 65535)`

### StreamPeerSocket
*Inherits: **StreamPeer < RefCounted < Object** | Inherited by: StreamPeerTCP, StreamPeerUDS*

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

**Methods**
- `void DisconnectFromHost()`
- `Status GetStatus()`
- `Error Poll()`

### StreamPeerTCP
*Inherits: **StreamPeerSocket < StreamPeer < RefCounted < Object***

A stream peer that handles TCP connections. This object can be used to connect to TCP servers, or also is returned by a TCP server.

**Methods**
- `Error Bind(int port, string host = "*")`
- `Error ConnectToHost(string host, int port)`
- `string GetConnectedHost()`
- `int GetConnectedPort()`
- `int GetLocalPort()`
- `void SetNoDelay(bool enabled)`

### StreamPeerTLS
*Inherits: **StreamPeer < RefCounted < Object***

A stream peer that handles TLS connections. This object can be used to connect to a TLS server or accept a single TLS client connection.

**Methods**
- `Error AcceptStream(StreamPeer stream, TLSOptions serverOptions)`
- `Error ConnectToStream(StreamPeer stream, string commonName, TLSOptions clientOptions = null)`
- `void DisconnectFromStream()`
- `Status GetStatus()`
- `StreamPeer GetStream()`
- `void Poll()`

### StreamPeerUDS
*Inherits: **StreamPeerSocket < StreamPeer < RefCounted < Object***

A stream peer that handles UNIX Domain Socket (UDS) connections. This object can be used to connect to UDS servers, or also is returned by a UDS server. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Methods**
- `Error Bind(string path)`
- `Error ConnectToHost(string path)`
- `string GetConnectedPath()`

### StreamPeer
*Inherits: **RefCounted < Object** | Inherited by: StreamPeerBuffer, StreamPeerExtension, StreamPeerGZIP, StreamPeerSocket, StreamPeerTLS*

StreamPeer is an abstract base class mostly used for stream-based protocols (such as TCP). It provides an API for sending and receiving data through streams as raw data or strings.

**Properties**
- `bool BigEndian` = `false`

**Methods**
- `int Get8()`
- `int Get16()`
- `int Get32()`
- `int Get64()`
- `int GetAvailableBytes()`
- `Godot.Collections.Array GetData(int bytes)`
- `float GetDouble()`
- `float GetFloat()`
- `float GetHalf()`
- `Godot.Collections.Array GetPartialData(int bytes)`
- `string GetString(int bytes = -1)`
- `int GetU8()`
- `int GetU16()`
- `int GetU32()`
- `int GetU64()`
- `string GetUtf8String(int bytes = -1)`
- `Variant GetVar(bool allowObjects = false)`
- `void Put8(int value)`
- `void Put16(int value)`
- `void Put32(int value)`
- `void Put64(int value)`
- `Error PutData(PackedByteArray data)`
- `void PutDouble(float value)`
- `void PutFloat(float value)`
- `void PutHalf(float value)`
- `Godot.Collections.Array PutPartialData(PackedByteArray data)`
- `void PutString(string value)`
- `void PutU8(int value)`
- `void PutU16(int value)`
- `void PutU32(int value)`
- `void PutU64(int value)`
- `void PutUtf8String(string value)`
- `void PutVar(Variant value, bool fullObjects = false)`

**C# Examples**
```csharp
PutData("Hello World".ToAsciiBuffer());
```
```csharp
PutData("Hello World".ToUtf8Buffer());
```

### TCPServer
*Inherits: **SocketServer < RefCounted < Object***

A TCP server. Listens to connections on a port and returns a StreamPeerTCP when it gets an incoming connection.

**Methods**
- `int GetLocalPort()`
- `Error Listen(int port, string bindAddress = "*")`
- `StreamPeerTCP TakeConnection()`

### TLSOptions
*Inherits: **RefCounted < Object***

TLSOptions abstracts the configuration options for the StreamPeerTLS and PacketPeerDTLS classes.

**Methods**
- `TLSOptions Client(X509Certificate trustedChain = null, string commonNameOverride = "") [static]`
- `TLSOptions ClientUnsafe(X509Certificate trustedChain = null) [static]`
- `string GetCommonNameOverride()`
- `X509Certificate GetOwnCertificate()`
- `CryptoKey GetPrivateKey()`
- `X509Certificate GetTrustedCaChain()`
- `bool IsServer()`
- `bool IsUnsafeClient()`
- `TLSOptions Server(CryptoKey key, X509Certificate certificate) [static]`

### UDPServer
*Inherits: **RefCounted < Object***

A simple server that opens a UDP socket and returns connected PacketPeerUDP upon receiving new packets. See also PacketPeerUDP.connect_to_host().

**Properties**
- `int MaxPendingConnections` = `16`

**Methods**
- `int GetLocalPort()`
- `bool IsConnectionAvailable()`
- `bool IsListening()`
- `Error Listen(int port, string bindAddress = "*")`
- `Error Poll()`
- `void Stop()`
- `PacketPeerUDP TakeConnection()`

**C# Examples**
```csharp
// ServerNode.cs
using Godot;
using System.Collections.Generic;

public partial class ServerNode : Node
{
    private UdpServer _server = new UdpServer();
    private List<PacketPeerUdp> _peers  = new List<PacketPeerUdp>();

    public override void _Ready()
    {
        _server.Listen(4242);
    }

    public override void _Process(double delta)
    {
        _server.Poll(); // Important!
        if (_server.IsConnectionAvailable())
        {
            PacketPeerUdp peer = _server.TakeConnection();
            byte[] packet = peer.GetPacket();
            GD.Print($"Accepted Peer: {peer.Ge
// ...
```
```csharp
// ClientNode.cs
using Godot;

public partial class ClientNode : Node
{
    private PacketPeerUdp _udp = new PacketPeerUdp();
    private bool _connected = false;

    public override void _Ready()
    {
        _udp.ConnectToHost("127.0.0.1", 4242);
    }

    public override void _Process(double delta)
    {
        if (!_connected)
        {
            // Try to contact server
            _udp.PutPacket("The Answer Is..42!".ToUtf8Buffer());
        }
        if (_udp.GetAvailablePacketCount() > 0)
        {
            GD.Print($"Connected: {_udp.GetPacket().GetStringFromUtf8()}");

// ...
```

### WebSocketMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

Base class for WebSocket server and client, allowing them to be used as multiplayer peer for the MultiplayerAPI.

**Properties**
- `PackedStringArray HandshakeHeaders` = `PackedStringArray()`
- `float HandshakeTimeout` = `3.0`
- `int InboundBufferSize` = `65535`
- `int MaxQueuedPackets` = `4096`
- `int OutboundBufferSize` = `65535`
- `PackedStringArray SupportedProtocols` = `PackedStringArray()`

**Methods**
- `Error CreateClient(string url, TLSOptions tlsClientOptions = null)`
- `Error CreateServer(int port, string bindAddress = "*", TLSOptions tlsServerOptions = null)`
- `WebSocketPeer GetPeer(int peerId)`
- `string GetPeerAddress(int id)`
- `int GetPeerPort(int id)`

### WebSocketPeer
*Inherits: **PacketPeer < RefCounted < Object***

This class represents WebSocket connection, and can be used as a WebSocket client (RFC 6455-compliant) or as a remote peer of a WebSocket server.

**Properties**
- `PackedStringArray HandshakeHeaders` = `PackedStringArray()`
- `float HeartbeatInterval` = `0.0`
- `int InboundBufferSize` = `65535`
- `int MaxQueuedPackets` = `4096`
- `int OutboundBufferSize` = `65535`
- `PackedStringArray SupportedProtocols` = `PackedStringArray()`

**Methods**
- `Error AcceptStream(StreamPeer stream)`
- `void Close(int code = 1000, string reason = "")`
- `Error ConnectToUrl(string url, TLSOptions tlsClientOptions = null)`
- `int GetCloseCode()`
- `string GetCloseReason()`
- `string GetConnectedHost()`
- `int GetConnectedPort()`
- `int GetCurrentOutboundBufferedAmount()`
- `State GetReadyState()`
- `string GetRequestedUrl()`
- `string GetSelectedProtocol()`
- `void Poll()`
- `Error Send(PackedByteArray message, WriteMode writeMode = 1)`
- `Error SendText(string message)`
- `void SetNoDelay(bool enabled)`
- `bool WasStringPacket()`

### X509Certificate
*Inherits: **Resource < RefCounted < Object***

The X509Certificate class represents an X509 certificate. Certificates can be loaded and saved like any other Resource.

**Methods**
- `Error Load(string path)`
- `Error LoadFromString(string string)`
- `Error Save(string path)`
- `string SaveToString()`
