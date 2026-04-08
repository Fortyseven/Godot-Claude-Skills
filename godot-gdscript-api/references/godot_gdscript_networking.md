# Godot 4 GDScript API Reference — Networking

> GDScript-only reference. 34 classes.

### AESContext
*Inherits: **RefCounted < Object***

This class holds the context information required for encryption and decryption operations with AES (Advanced Encryption Standard). Both AES-ECB and AES-CBC modes are supported.

**Methods**
- `void finish()`
- `PackedByteArray get_iv_state()`
- `Error start(mode: Mode, key: PackedByteArray, iv: PackedByteArray = PackedByteArray())`
- `PackedByteArray update(src: PackedByteArray)`

**GDScript Examples**
```gdscript
extends Node

var aes = AESContext.new()

func _ready():
    var key = "My secret key!!!" # Key must be either 16 or 32 bytes.
    var data = "My secret text!!" # Data size must be multiple of 16 bytes, apply padding if needed.
    # Encrypt ECB
    aes.start(AESContext.MODE_ECB_ENCRYPT, key.to_utf8_buffer())
    var encrypted = aes.update(data.to_utf8_buffer())
    aes.finish()
    # Decrypt ECB
    aes.start(AESContext.MODE_ECB_DECRYPT, key.to_utf8_buffer())
    var decrypted = aes.update(encrypted)
    aes.finish()
    # Check ECB
    assert(decrypted == data.to_utf8_buffer())

    var iv =
# ...
```

### CryptoKey
*Inherits: **Resource < RefCounted < Object***

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any other Resource.

**Methods**
- `bool is_public_only() const`
- `Error load(path: String, public_only: bool = false)`
- `Error load_from_string(string_key: String, public_only: bool = false)`
- `Error save(path: String, public_only: bool = false)`
- `String save_to_string(public_only: bool = false)`

### Crypto
*Inherits: **RefCounted < Object***

The Crypto class provides access to advanced cryptographic functionalities.

**Methods**
- `bool constant_time_compare(trusted: PackedByteArray, received: PackedByteArray)`
- `PackedByteArray decrypt(key: CryptoKey, ciphertext: PackedByteArray)`
- `PackedByteArray encrypt(key: CryptoKey, plaintext: PackedByteArray)`
- `PackedByteArray generate_random_bytes(size: int)`
- `CryptoKey generate_rsa(size: int)`
- `X509Certificate generate_self_signed_certificate(key: CryptoKey, issuer_name: String = "CN=myserver,O=myorganisation,C=IT", not_before: String = "20140101000000", not_after: String = "20340101000000")`
- `PackedByteArray hmac_digest(hash_type: HashType, key: PackedByteArray, msg: PackedByteArray)`
- `PackedByteArray sign(hash_type: HashType, hash: PackedByteArray, key: CryptoKey)`
- `bool verify(hash_type: HashType, hash: PackedByteArray, signature: PackedByteArray, key: CryptoKey)`

**GDScript Examples**
```gdscript
var crypto = Crypto.new()

# Generate new RSA key.
var key = crypto.generate_rsa(4096)

# Generate new self-signed certificate with the given key.
var cert = crypto.generate_self_signed_certificate(key, "CN=mydomain.com,O=My Game Company,C=IT")

# Save key and certificate in the user folder.
key.save("user://generated.key")
cert.save("user://generated.crt")

# Encryption
var data = "Some data"
var encrypted = crypto.encrypt(key, data.to_utf8_buffer())

# Decryption
var decrypted = crypto.decrypt(key, encrypted)

# Signing
var signature = crypto.sign(HashingContext.HASH_SHA256, data.sha256_buff
# ...
```
```gdscript
var crypto = Crypto.new()
# Generate 4096 bits RSA key.
var key = crypto.generate_rsa(4096)
# Generate self-signed certificate using the given key.
var cert = crypto.generate_self_signed_certificate(key, "CN=example.com,O=A Game Company,C=IT")
```

### DTLSServer
*Inherits: **RefCounted < Object***

This class is used to store the state of a DTLS server. Upon setup() it converts connected PacketPeerUDP to PacketPeerDTLS accepting them via take_connection() as DTLS clients. Under the hood, this class is used to store the DTLS state and cookies of the server. The reason of why the state and cookies are needed is outside of the scope of this documentation.

**Methods**
- `Error setup(server_options: TLSOptions)`
- `PacketPeerDTLS take_connection(udp_peer: PacketPeerUDP)`

**GDScript Examples**
```gdscript
# server_node.gd
extends Node

var dtls = DTLSServer.new()
var server = UDPServer.new()
var peers = []

func _ready():
    server.listen(4242)
    var key = load("key.key") # Your private key.
    var cert = load("cert.crt") # Your X509 certificate.
    dtls.setup(TlsOptions.server(key, cert))

func _process(delta):
    while server.is_connection_available():
        var peer = server.take_connection()
        var dtls_peer = dtls.take_connection(peer)
        if dtls_peer.get_status() != PacketPeerDTLS.STATUS_HANDSHAKING:
            continue # It is normal that 50% of the connections fails d
# ...
```
```gdscript
# client_node.gd
extends Node

var dtls = PacketPeerDTLS.new()
var udp = PacketPeerUDP.new()
var connected = false

func _ready():
    udp.connect_to_host("127.0.0.1", 4242)
    dtls.connect_to_peer(udp, false) # Use true in production for certificate validation!

func _process(delta):
    dtls.poll()
    if dtls.get_status() == PacketPeerDTLS.STATUS_CONNECTED:
        if !connected:
            # Try to contact server
            dtls.put_packet("The answer is... 42!".to_utf8_buffer())
        while dtls.get_available_packet_count() > 0:
            print("Connected: %s" % dtls.get_packet().g
# ...
```

### ENetConnection
*Inherits: **RefCounted < Object***

ENet's purpose is to provide a relatively thin, simple and robust network communication layer on top of UDP (User Datagram Protocol).

**Methods**
- `void bandwidth_limit(in_bandwidth: int = 0, out_bandwidth: int = 0)`
- `void broadcast(channel: int, packet: PackedByteArray, flags: int)`
- `void channel_limit(limit: int)`
- `void compress(mode: CompressionMode)`
- `ENetPacketPeer connect_to_host(address: String, port: int, channels: int = 0, data: int = 0)`
- `Error create_host(max_peers: int = 32, max_channels: int = 0, in_bandwidth: int = 0, out_bandwidth: int = 0)`
- `Error create_host_bound(bind_address: String, bind_port: int, max_peers: int = 32, max_channels: int = 0, in_bandwidth: int = 0, out_bandwidth: int = 0)`
- `void destroy()`
- `Error dtls_client_setup(hostname: String, client_options: TLSOptions = null)`
- `Error dtls_server_setup(server_options: TLSOptions)`
- `void flush()`
- `int get_local_port() const`
- `int get_max_channels() const`
- `Array[ENetPacketPeer] get_peers()`
- `float pop_statistic(statistic: HostStatistic)`
- `void refuse_new_connections(refuse: bool)`
- `Array service(timeout: int = 0)`
- `void socket_send(destination_address: String, destination_port: int, packet: PackedByteArray)`

### ENetMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

A MultiplayerPeer implementation that should be passed to MultiplayerAPI.multiplayer_peer after being initialized as either a client, server, or mesh. Events can then be handled by connecting to MultiplayerAPI signals. See ENetConnection for more information on the ENet library wrapper.

**Properties**
- `ENetConnection host`

**Methods**
- `Error add_mesh_peer(peer_id: int, host: ENetConnection)`
- `Error create_client(address: String, port: int, channel_count: int = 0, in_bandwidth: int = 0, out_bandwidth: int = 0, local_port: int = 0)`
- `Error create_mesh(unique_id: int)`
- `Error create_server(port: int, max_clients: int = 32, max_channels: int = 0, in_bandwidth: int = 0, out_bandwidth: int = 0)`
- `ENetPacketPeer get_peer(id: int) const`
- `void set_bind_ip(ip: String)`

### ENetPacketPeer
*Inherits: **PacketPeer < RefCounted < Object***

A PacketPeer implementation representing a peer of an ENetConnection.

**Methods**
- `int get_channels() const`
- `int get_packet_flags() const`
- `String get_remote_address() const`
- `int get_remote_port() const`
- `PeerState get_state() const`
- `float get_statistic(statistic: PeerStatistic)`
- `bool is_active() const`
- `void peer_disconnect(data: int = 0)`
- `void peer_disconnect_later(data: int = 0)`
- `void peer_disconnect_now(data: int = 0)`
- `void ping()`
- `void ping_interval(ping_interval: int)`
- `void reset()`
- `Error send(channel: int, packet: PackedByteArray, flags: int)`
- `void set_timeout(timeout: int, timeout_min: int, timeout_max: int)`
- `void throttle_configure(interval: int, acceleration: int, deceleration: int)`

### HTTPClient
*Inherits: **RefCounted < Object***

Hyper-text transfer protocol client (sometimes called "User Agent"). Used to make HTTP requests to download web content, upload files and other data or to communicate with various services, among other use cases.

**Properties**
- `bool blocking_mode_enabled` = `false`
- `StreamPeer connection`
- `int read_chunk_size` = `65536`

**Methods**
- `void close()`
- `Error connect_to_host(host: String, port: int = -1, tls_options: TLSOptions = null)`
- `int get_response_body_length() const`
- `int get_response_code() const`
- `PackedStringArray get_response_headers()`
- `Dictionary get_response_headers_as_dictionary()`
- `Status get_status() const`
- `bool has_response() const`
- `bool is_response_chunked() const`
- `Error poll()`
- `String query_string_from_dict(fields: Dictionary)`
- `PackedByteArray read_response_body_chunk()`
- `Error request(method: Method, url: String, headers: PackedStringArray, body: String = "")`
- `Error request_raw(method: Method, url: String, headers: PackedStringArray, body: PackedByteArray)`
- `void set_http_proxy(host: String, port: int)`
- `void set_https_proxy(host: String, port: int)`

**GDScript Examples**
```gdscript
var fields = { "username": "user", "password": "pass" }
var query_string = http_client.query_string_from_dict(fields)
# Returns "username=user&password=pass"
```
```gdscript
var fields = { "single": 123, "not_valued": null, "multiple": [22, 33, 44] }
var query_string = http_client.query_string_from_dict(fields)
# Returns "single=123&not_valued&multiple=22&multiple=33&multiple=44"
```

### HTTPRequest
*Inherits: **Node < Object***

A node with the ability to send HTTP requests. Uses HTTPClient internally.

**Properties**
- `bool accept_gzip` = `true`
- `int body_size_limit` = `-1`
- `int download_chunk_size` = `65536`
- `String download_file` = `""`
- `int max_redirects` = `8`
- `float timeout` = `0.0`
- `bool use_threads` = `false`

**Methods**
- `void cancel_request()`
- `int get_body_size() const`
- `int get_downloaded_bytes() const`
- `Status get_http_client_status() const`
- `Error request(url: String, custom_headers: PackedStringArray = PackedStringArray(), method: Method = 0, request_data: String = "")`
- `Error request_raw(url: String, custom_headers: PackedStringArray = PackedStringArray(), method: Method = 0, request_data_raw: PackedByteArray = PackedByteArray())`
- `void set_http_proxy(host: String, port: int)`
- `void set_https_proxy(host: String, port: int)`
- `void set_tls_options(client_options: TLSOptions)`

**GDScript Examples**
```gdscript
func _ready():
    # Create an HTTP request node and connect its completion signal.
    var http_request = HTTPRequest.new()
    add_child(http_request)
    http_request.request_completed.connect(self._http_request_completed)

    # Perform a GET request. The URL below returns JSON as of writing.
    var error = http_request.request("https://httpbin.org/get")
    if error != OK:
        push_error("An error occurred in the HTTP request.")

    # Perform a POST request. The URL below returns JSON as of writing.
    # Note: Don't make simultaneous requests using a single HTTPRequest node.
    #
# ...
```
```gdscript
func _ready():
    # Create an HTTP request node and connect its completion signal.
    var http_request = HTTPRequest.new()
    add_child(http_request)
    http_request.request_completed.connect(self._http_request_completed)

    # Perform the HTTP request. The URL below returns a PNG image as of writing.
    var error = http_request.request("https://placehold.co/512.png")
    if error != OK:
        push_error("An error occurred in the HTTP request.")

# Called when the HTTP request is completed.
func _http_request_completed(result, response_code, headers, body):
    if result != HTTPRequest
# ...
```

### HashingContext
*Inherits: **RefCounted < Object***

The HashingContext class provides an interface for computing cryptographic hashes over multiple iterations. Useful for computing hashes of big files (so you don't have to load them all in memory), network streams, and data streams in general (so you don't have to hold buffers).

**Methods**
- `PackedByteArray finish()`
- `Error start(type: HashType)`
- `Error update(chunk: PackedByteArray)`

**GDScript Examples**
```gdscript
const CHUNK_SIZE = 1024

func hash_file(path):
    # Check that file exists.
    if not FileAccess.file_exists(path):
        return
    # Start an SHA-256 context.
    var ctx = HashingContext.new()
    ctx.start(HashingContext.HASH_SHA256)
    # Open the file to hash.
    var file = FileAccess.open(path, FileAccess.READ)
    # Update the context after reading each chunk.
    while file.get_position() < file.get_length():
        var remaining = file.get_length() - file.get_position()
        ctx.update(file.get_buffer(min(remaining, CHUNK_SIZE)))
    # Get the computed hash.
    var res = ct
# ...
```

### MultiplayerAPIExtension
*Inherits: **MultiplayerAPI < RefCounted < Object***

This class can be used to extend or replace the default MultiplayerAPI implementation via script or extensions.

**Methods**
- `MultiplayerPeer _get_multiplayer_peer() virtual`
- `PackedInt32Array _get_peer_ids() virtual const`
- `int _get_remote_sender_id() virtual const`
- `int _get_unique_id() virtual const`
- `Error _object_configuration_add(object: Object, configuration: Variant) virtual`
- `Error _object_configuration_remove(object: Object, configuration: Variant) virtual`
- `Error _poll() virtual`
- `Error _rpc(peer: int, object: Object, method: StringName, args: Array) virtual`
- `void _set_multiplayer_peer(multiplayer_peer: MultiplayerPeer) virtual`

**GDScript Examples**
```gdscript
extends MultiplayerAPIExtension
class_name LogMultiplayer

# We want to extend the default SceneMultiplayer.
var base_multiplayer = SceneMultiplayer.new()

func _init():
    # Just passthrough base signals (copied to var to avoid cyclic reference)
    var cts = connected_to_server
    var cf = connection_failed
    var sd = server_disconnected
    var pc = peer_connected
    var pd = peer_disconnected
    base_multiplayer.connected_to_server.connect(func(): cts.emit())
    base_multiplayer.connection_failed.connect(func(): cf.emit())
    base_multiplayer.server_disconnected.connect(func(): sd.
# ...
```
```gdscript
# autoload.gd
func _enter_tree():
    # Sets our custom multiplayer as the main one in SceneTree.
    get_tree().set_multiplayer(LogMultiplayer.new())
```

### MultiplayerAPI
*Inherits: **RefCounted < Object** | Inherited by: MultiplayerAPIExtension, SceneMultiplayer*

Base class for high-level multiplayer API implementations. See also MultiplayerPeer.

**Properties**
- `MultiplayerPeer multiplayer_peer`

**Methods**
- `MultiplayerAPI create_default_interface() static`
- `StringName get_default_interface() static`
- `PackedInt32Array get_peers()`
- `int get_remote_sender_id()`
- `int get_unique_id()`
- `bool has_multiplayer_peer()`
- `bool is_server()`
- `Error object_configuration_add(object: Object, configuration: Variant)`
- `Error object_configuration_remove(object: Object, configuration: Variant)`
- `Error poll()`
- `Error rpc(peer: int, object: Object, method: StringName, arguments: Array = [])`
- `void set_default_interface(interface_name: StringName) static`

### MultiplayerPeerExtension
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods below must be implemented to have a working custom multiplayer implementation. See also MultiplayerAPI.

**Methods**
- `void _close() virtual required`
- `void _disconnect_peer(p_peer: int, p_force: bool) virtual required`
- `int _get_available_packet_count() virtual required const`
- `ConnectionStatus _get_connection_status() virtual required const`
- `int _get_max_packet_size() virtual required const`
- `Error _get_packet(r_buffer: const uint8_t **, r_buffer_size: int32_t*) virtual`
- `int _get_packet_channel() virtual required const`
- `TransferMode _get_packet_mode() virtual required const`
- `int _get_packet_peer() virtual required const`
- `PackedByteArray _get_packet_script() virtual`
- `int _get_transfer_channel() virtual required const`
- `TransferMode _get_transfer_mode() virtual required const`
- `int _get_unique_id() virtual required const`
- `bool _is_refusing_new_connections() virtual const`
- `bool _is_server() virtual required const`
- `bool _is_server_relay_supported() virtual const`
- `void _poll() virtual required`
- `Error _put_packet(p_buffer: const uint8_t*, p_buffer_size: int) virtual`
- `Error _put_packet_script(p_buffer: PackedByteArray) virtual`
- `void _set_refuse_new_connections(p_enable: bool) virtual`
- `void _set_target_peer(p_peer: int) virtual required`
- `void _set_transfer_channel(p_channel: int) virtual required`
- `void _set_transfer_mode(p_mode: TransferMode) virtual required`

### MultiplayerPeer
*Inherits: **PacketPeer < RefCounted < Object** | Inherited by: ENetMultiplayerPeer, MultiplayerPeerExtension, OfflineMultiplayerPeer, WebRTCMultiplayerPeer, WebSocketMultiplayerPeer*

Manages the connection with one or more remote peers acting as server or client and assigning unique IDs to each of them. See also MultiplayerAPI.

**Properties**
- `bool refuse_new_connections` = `false`
- `int transfer_channel` = `0`
- `TransferMode transfer_mode` = `2`

**Methods**
- `void close()`
- `void disconnect_peer(peer: int, force: bool = false)`
- `int generate_unique_id() const`
- `ConnectionStatus get_connection_status() const`
- `int get_packet_channel() const`
- `TransferMode get_packet_mode() const`
- `int get_packet_peer() const`
- `int get_unique_id() const`
- `bool is_server_relay_supported() const`
- `void poll()`
- `void set_target_peer(id: int)`

### PacketPeerDTLS
*Inherits: **PacketPeer < RefCounted < Object***

This class represents a DTLS peer connection. It can be used to connect to a DTLS server, and is returned by DTLSServer.take_connection().

**Methods**
- `Error connect_to_peer(packet_peer: PacketPeerUDP, hostname: String, client_options: TLSOptions = null)`
- `void disconnect_from_peer()`
- `Status get_status() const`
- `void poll()`

### PacketPeerExtension
*Inherits: **PacketPeer < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `int _get_available_packet_count() virtual required const`
- `int _get_max_packet_size() virtual required const`
- `Error _get_packet(r_buffer: const uint8_t **, r_buffer_size: int32_t*) virtual`
- `Error _put_packet(p_buffer: const uint8_t*, p_buffer_size: int) virtual`

### PacketPeerStream
*Inherits: **PacketPeer < RefCounted < Object***

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

**Properties**
- `int input_buffer_max_size` = `65532`
- `int output_buffer_max_size` = `65532`
- `StreamPeer stream_peer`

### PacketPeerUDP
*Inherits: **PacketPeer < RefCounted < Object***

UDP packet peer. Can be used to send and receive raw UDP packets as well as Variants.

**Methods**
- `Error bind(port: int, bind_address: String = "*", recv_buf_size: int = 65536)`
- `void close()`
- `Error connect_to_host(host: String, port: int)`
- `int get_local_port() const`
- `String get_packet_ip() const`
- `int get_packet_port() const`
- `bool is_bound() const`
- `bool is_socket_connected() const`
- `Error join_multicast_group(multicast_address: String, interface_name: String)`
- `Error leave_multicast_group(multicast_address: String, interface_name: String)`
- `void set_broadcast_enabled(enabled: bool)`
- `Error set_dest_address(host: String, port: int)`
- `Error wait()`

**GDScript Examples**
```gdscript
socket = PacketPeerUDP.new()
# Server
socket.set_dest_address("127.0.0.1", 789)
socket.put_packet("Time to stop".to_ascii_buffer())

# Client
while socket.wait() == OK:
    var data = socket.get_packet().get_string_from_ascii()
    if data == "Time to stop":
        return
```
```gdscript
var peer = PacketPeerUDP.new()

# Optionally, you can select the local port used to send the packet.
peer.bind(4444)

peer.set_dest_address("1.1.1.1", 4433)
peer.put_packet("hello".to_utf8_buffer())
```

### PacketPeer
*Inherits: **RefCounted < Object** | Inherited by: ENetPacketPeer, MultiplayerPeer, PacketPeerDTLS, PacketPeerExtension, PacketPeerStream, PacketPeerUDP, ...*

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low-level bytes or having to worry about network ordering.

**Properties**
- `int encode_buffer_max_size` = `8388608`

**Methods**
- `int get_available_packet_count() const`
- `PackedByteArray get_packet()`
- `Error get_packet_error() const`
- `Variant get_var(allow_objects: bool = false)`
- `Error put_packet(buffer: PackedByteArray)`
- `Error put_var(var: Variant, full_objects: bool = false)`

### SceneMultiplayer
*Inherits: **MultiplayerAPI < RefCounted < Object***

This class is the default implementation of MultiplayerAPI, used to provide multiplayer functionalities in Godot Engine.

**Properties**
- `bool allow_object_decoding` = `false`
- `Callable auth_callback` = `Callable()`
- `float auth_timeout` = `3.0`
- `int max_delta_packet_size` = `65535`
- `int max_sync_packet_size` = `1350`
- `bool refuse_new_connections` = `false`
- `NodePath root_path` = `NodePath("")`
- `bool server_relay` = `true`

**Methods**
- `void clear()`
- `Error complete_auth(id: int)`
- `void disconnect_peer(id: int)`
- `PackedInt32Array get_authenticating_peers()`
- `Error send_auth(id: int, data: PackedByteArray)`
- `Error send_bytes(bytes: PackedByteArray, id: int = 0, mode: TransferMode = 2, channel: int = 0)`

### StreamPeerBuffer
*Inherits: **StreamPeer < RefCounted < Object***

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, FileAccess can be used directly.

**Properties**
- `PackedByteArray data_array` = `PackedByteArray()`

**Methods**
- `void clear()`
- `StreamPeerBuffer duplicate() const`
- `int get_position() const`
- `int get_size() const`
- `void resize(size: int)`
- `void seek(position: int)`

### StreamPeerExtension
*Inherits: **StreamPeer < RefCounted < Object***

There is currently no description for this class. Please help us by contributing one!

**Methods**
- `int _get_available_bytes() virtual required const`
- `Error _get_data(r_buffer: uint8_t*, r_bytes: int, r_received: int32_t*) virtual`
- `Error _get_partial_data(r_buffer: uint8_t*, r_bytes: int, r_received: int32_t*) virtual`
- `Error _put_data(p_data: const uint8_t*, p_bytes: int, r_sent: int32_t*) virtual`
- `Error _put_partial_data(p_data: const uint8_t*, p_bytes: int, r_sent: int32_t*) virtual`

### StreamPeerGZIP
*Inherits: **StreamPeer < RefCounted < Object***

This class allows to compress or decompress data using GZIP/deflate in a streaming fashion. This is particularly useful when compressing or decompressing files that have to be sent through the network without needing to allocate them all in memory.

**Methods**
- `void clear()`
- `Error finish()`
- `Error start_compression(use_deflate: bool = false, buffer_size: int = 65535)`
- `Error start_decompression(use_deflate: bool = false, buffer_size: int = 65535)`

### StreamPeerSocket
*Inherits: **StreamPeer < RefCounted < Object** | Inherited by: StreamPeerTCP, StreamPeerUDS*

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

**Methods**
- `void disconnect_from_host()`
- `Status get_status() const`
- `Error poll()`

### StreamPeerTCP
*Inherits: **StreamPeerSocket < StreamPeer < RefCounted < Object***

A stream peer that handles TCP connections. This object can be used to connect to TCP servers, or also is returned by a TCP server.

**Methods**
- `Error bind(port: int, host: String = "*")`
- `Error connect_to_host(host: String, port: int)`
- `String get_connected_host() const`
- `int get_connected_port() const`
- `int get_local_port() const`
- `void set_no_delay(enabled: bool)`

### StreamPeerTLS
*Inherits: **StreamPeer < RefCounted < Object***

A stream peer that handles TLS connections. This object can be used to connect to a TLS server or accept a single TLS client connection.

**Methods**
- `Error accept_stream(stream: StreamPeer, server_options: TLSOptions)`
- `Error connect_to_stream(stream: StreamPeer, common_name: String, client_options: TLSOptions = null)`
- `void disconnect_from_stream()`
- `Status get_status() const`
- `StreamPeer get_stream() const`
- `void poll()`

### StreamPeerUDS
*Inherits: **StreamPeerSocket < StreamPeer < RefCounted < Object***

A stream peer that handles UNIX Domain Socket (UDS) connections. This object can be used to connect to UDS servers, or also is returned by a UDS server. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Methods**
- `Error bind(path: String)`
- `Error connect_to_host(path: String)`
- `String get_connected_path() const`

### StreamPeer
*Inherits: **RefCounted < Object** | Inherited by: StreamPeerBuffer, StreamPeerExtension, StreamPeerGZIP, StreamPeerSocket, StreamPeerTLS*

StreamPeer is an abstract base class mostly used for stream-based protocols (such as TCP). It provides an API for sending and receiving data through streams as raw data or strings.

**Properties**
- `bool big_endian` = `false`

**Methods**
- `int get_8()`
- `int get_16()`
- `int get_32()`
- `int get_64()`
- `int get_available_bytes() const`
- `Array get_data(bytes: int)`
- `float get_double()`
- `float get_float()`
- `float get_half()`
- `Array get_partial_data(bytes: int)`
- `String get_string(bytes: int = -1)`
- `int get_u8()`
- `int get_u16()`
- `int get_u32()`
- `int get_u64()`
- `String get_utf8_string(bytes: int = -1)`
- `Variant get_var(allow_objects: bool = false)`
- `void put_8(value: int)`
- `void put_16(value: int)`
- `void put_32(value: int)`
- `void put_64(value: int)`
- `Error put_data(data: PackedByteArray)`
- `void put_double(value: float)`
- `void put_float(value: float)`
- `void put_half(value: float)`
- `Array put_partial_data(data: PackedByteArray)`
- `void put_string(value: String)`
- `void put_u8(value: int)`
- `void put_u16(value: int)`
- `void put_u32(value: int)`
- `void put_u64(value: int)`
- `void put_utf8_string(value: String)`
- `void put_var(value: Variant, full_objects: bool = false)`

**GDScript Examples**
```gdscript
put_data("Hello world".to_ascii_buffer())
```
```gdscript
put_data("Hello world".to_utf8_buffer())
```

### TCPServer
*Inherits: **SocketServer < RefCounted < Object***

A TCP server. Listens to connections on a port and returns a StreamPeerTCP when it gets an incoming connection.

**Methods**
- `int get_local_port() const`
- `Error listen(port: int, bind_address: String = "*")`
- `StreamPeerTCP take_connection()`

### TLSOptions
*Inherits: **RefCounted < Object***

TLSOptions abstracts the configuration options for the StreamPeerTLS and PacketPeerDTLS classes.

**Methods**
- `TLSOptions client(trusted_chain: X509Certificate = null, common_name_override: String = "") static`
- `TLSOptions client_unsafe(trusted_chain: X509Certificate = null) static`
- `String get_common_name_override() const`
- `X509Certificate get_own_certificate() const`
- `CryptoKey get_private_key() const`
- `X509Certificate get_trusted_ca_chain() const`
- `bool is_server() const`
- `bool is_unsafe_client() const`
- `TLSOptions server(key: CryptoKey, certificate: X509Certificate) static`

**GDScript Examples**
```gdscript
# Create a TLS client configuration which uses our custom trusted CA chain.
var client_trusted_cas = load("res://my_trusted_cas.crt")
var client_tls_options = TLSOptions.client(client_trusted_cas)

# Create a TLS server configuration.
var server_certs = load("res://my_server_cas.crt")
var server_key = load("res://my_server_key.key")
var server_tls_options = TLSOptions.server(server_key, server_certs)
```

### UDPServer
*Inherits: **RefCounted < Object***

A simple server that opens a UDP socket and returns connected PacketPeerUDP upon receiving new packets. See also PacketPeerUDP.connect_to_host().

**Properties**
- `int max_pending_connections` = `16`

**Methods**
- `int get_local_port() const`
- `bool is_connection_available() const`
- `bool is_listening() const`
- `Error listen(port: int, bind_address: String = "*")`
- `Error poll()`
- `void stop()`
- `PacketPeerUDP take_connection()`

**GDScript Examples**
```gdscript
# server_node.gd
class_name ServerNode
extends Node

var server = UDPServer.new()
var peers = []

func _ready():
    server.listen(4242)

func _process(delta):
    server.poll() # Important!
    if server.is_connection_available():
        var peer = server.take_connection()
        var packet = peer.get_packet()
        print("Accepted peer: %s:%s" % [peer.get_packet_ip(), peer.get_packet_port()])
        print("Received data: %s" % [packet.get_string_from_utf8()])
        # Reply so it knows we received the message.
        peer.put_packet(packet)
        # Keep a reference so we can keep co
# ...
```
```gdscript
# client_node.gd
class_name ClientNode
extends Node

var udp = PacketPeerUDP.new()
var connected = false

func _ready():
    udp.connect_to_host("127.0.0.1", 4242)

func _process(delta):
    if !connected:
        # Try to contact server
        udp.put_packet("The answer is... 42!".to_utf8_buffer())
    if udp.get_available_packet_count() > 0:
        print("Connected: %s" % udp.get_packet().get_string_from_utf8())
        connected = true
```

### WebSocketMultiplayerPeer
*Inherits: **MultiplayerPeer < PacketPeer < RefCounted < Object***

Base class for WebSocket server and client, allowing them to be used as multiplayer peer for the MultiplayerAPI.

**Properties**
- `PackedStringArray handshake_headers` = `PackedStringArray()`
- `float handshake_timeout` = `3.0`
- `int inbound_buffer_size` = `65535`
- `int max_queued_packets` = `4096`
- `int outbound_buffer_size` = `65535`
- `PackedStringArray supported_protocols` = `PackedStringArray()`

**Methods**
- `Error create_client(url: String, tls_client_options: TLSOptions = null)`
- `Error create_server(port: int, bind_address: String = "*", tls_server_options: TLSOptions = null)`
- `WebSocketPeer get_peer(peer_id: int) const`
- `String get_peer_address(id: int) const`
- `int get_peer_port(id: int) const`

### WebSocketPeer
*Inherits: **PacketPeer < RefCounted < Object***

This class represents WebSocket connection, and can be used as a WebSocket client (RFC 6455-compliant) or as a remote peer of a WebSocket server.

**Properties**
- `PackedStringArray handshake_headers` = `PackedStringArray()`
- `float heartbeat_interval` = `0.0`
- `int inbound_buffer_size` = `65535`
- `int max_queued_packets` = `4096`
- `int outbound_buffer_size` = `65535`
- `PackedStringArray supported_protocols` = `PackedStringArray()`

**Methods**
- `Error accept_stream(stream: StreamPeer)`
- `void close(code: int = 1000, reason: String = "")`
- `Error connect_to_url(url: String, tls_client_options: TLSOptions = null)`
- `int get_close_code() const`
- `String get_close_reason() const`
- `String get_connected_host() const`
- `int get_connected_port() const`
- `int get_current_outbound_buffered_amount() const`
- `State get_ready_state() const`
- `String get_requested_url() const`
- `String get_selected_protocol() const`
- `void poll()`
- `Error send(message: PackedByteArray, write_mode: WriteMode = 1)`
- `Error send_text(message: String)`
- `void set_no_delay(enabled: bool)`
- `bool was_string_packet() const`

**GDScript Examples**
```gdscript
extends Node

var socket = WebSocketPeer.new()

func _ready():
    socket.connect_to_url("wss://example.com")

func _process(delta):
    socket.poll()
    var state = socket.get_ready_state()
    if state == WebSocketPeer.STATE_OPEN:
        while socket.get_available_packet_count():
            print("Packet: ", socket.get_packet())
    elif state == WebSocketPeer.STATE_CLOSING:
        # Keep polling to achieve proper close.
        pass
    elif state == WebSocketPeer.STATE_CLOSED:
        var code = socket.get_close_code()
        var reason = socket.get_close_reason()
        print("WebSo
# ...
```

### X509Certificate
*Inherits: **Resource < RefCounted < Object***

The X509Certificate class represents an X509 certificate. Certificates can be loaded and saved like any other Resource.

**Methods**
- `Error load(path: String)`
- `Error load_from_string(string: String)`
- `Error save(path: String)`
- `String save_to_string()`
