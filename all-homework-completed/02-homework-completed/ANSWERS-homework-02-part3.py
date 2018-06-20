# Homework 2, Part 3 
# ANSWER KEY

import json

data = json.loads("{\"tracks\":[{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1YxmW7DO2dM05gwMKTbr7l\"},\"href\":\"https://api.spotify.com/v1/albums/1YxmW7DO2dM05gwMKTbr7l\",\"id\":\"1YxmW7DO2dM05gwMKTbr7l\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Fake Love\",\"type\":\"album\",\"uri\":\"spotify:album:1YxmW7DO2dM05gwMKTbr7l\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":207813,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600333\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/6NMNgWgEAzde5M8U3lc6FN\"},\"href\":\"https://api.spotify.com/v1/tracks/6NMNgWgEAzde5M8U3lc6FN\",\"id\":\"6NMNgWgEAzde5M8U3lc6FN\",\"name\":\"Fake Love\",\"popularity\":90,\"preview_url\":\"https://p.scdn.co/mp3-preview/b1c79b52128cc45a962cb87ba5a616ea6a435356?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:6NMNgWgEAzde5M8U3lc6FN\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3tVQdUvClmAT7URs9V3rsp\"},\"href\":\"https://api.spotify.com/v1/artists/3tVQdUvClmAT7URs9V3rsp\",\"id\":\"3tVQdUvClmAT7URs9V3rsp\",\"name\":\"WizKid\",\"type\":\"artist\",\"uri\":\"spotify:artist:3tVQdUvClmAT7URs9V3rsp\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/77DAFfvm3O9zT5dIoG0eIO\"},\"href\":\"https://api.spotify.com/v1/artists/77DAFfvm3O9zT5dIoG0eIO\",\"id\":\"77DAFfvm3O9zT5dIoG0eIO\",\"name\":\"Kyla\",\"type\":\"artist\",\"uri\":\"spotify:artist:77DAFfvm3O9zT5dIoG0eIO\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":173986,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51600028\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/12VWzyPDBCc8fqeWCAfNwR\"},\"href\":\"https://api.spotify.com/v1/tracks/12VWzyPDBCc8fqeWCAfNwR\",\"id\":\"12VWzyPDBCc8fqeWCAfNwR\",\"name\":\"One Dance\",\"popularity\":84,\"preview_url\":\"https://p.scdn.co/mp3-preview/98f60b086bb1da2ca2e4c217331b8c8cc801358d?cid=null\",\"track_number\":12,\"type\":\"track\",\"uri\":\"spotify:track:12VWzyPDBCc8fqeWCAfNwR\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/2z3NlPY0n0gHJPCPqrzA6V\"},\"href\":\"https://api.spotify.com/v1/albums/2z3NlPY0n0gHJPCPqrzA6V\",\"id\":\"2z3NlPY0n0gHJPCPqrzA6V\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Sneakin’\",\"type\":\"album\",\"uri\":\"spotify:album:2z3NlPY0n0gHJPCPqrzA6V\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1URnnhqYAYcrqrcwql10ft\"},\"href\":\"https://api.spotify.com/v1/artists/1URnnhqYAYcrqrcwql10ft\",\"id\":\"1URnnhqYAYcrqrcwql10ft\",\"name\":\"21 Savage\",\"type\":\"artist\",\"uri\":\"spotify:artist:1URnnhqYAYcrqrcwql10ft\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":251333,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600337\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4ckuS4Nj4FZ7i3Def3Br8W\"},\"href\":\"https://api.spotify.com/v1/tracks/4ckuS4Nj4FZ7i3Def3Br8W\",\"id\":\"4ckuS4Nj4FZ7i3Def3Br8W\",\"name\":\"Sneakin’\",\"popularity\":82,\"preview_url\":\"https://p.scdn.co/mp3-preview/4fa89ace286252c33a1ca0d36e7555d6a451a2db?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:4ckuS4Nj4FZ7i3Def3Br8W\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H\"},\"href\":\"https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H\",\"id\":\"5pKCCKE2ajJHZ9KAiaK11H\",\"name\":\"Rihanna\",\"type\":\"artist\",\"uri\":\"spotify:artist:5pKCCKE2ajJHZ9KAiaK11H\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":263373,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600088\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/7fJtPlEZKxu6gvkfBFc5tW\"},\"href\":\"https://api.spotify.com/v1/tracks/7fJtPlEZKxu6gvkfBFc5tW\",\"id\":\"7fJtPlEZKxu6gvkfBFc5tW\",\"name\":\"Too Good\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/e702c76de627c3fb04da1bcbf6a8b53c3326a0cc?cid=null\",\"track_number\":16,\"type\":\"track\",\"uri\":\"spotify:track:7fJtPlEZKxu6gvkfBFc5tW\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":245226,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600080\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4CpKEkdGbOJV51cSvx7SoG\"},\"href\":\"https://api.spotify.com/v1/tracks/4CpKEkdGbOJV51cSvx7SoG\",\"id\":\"4CpKEkdGbOJV51cSvx7SoG\",\"name\":\"Controlla\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/c5b5845dc83410f5731e395c5a725d6b6e94ff69?cid=null\",\"track_number\":11,\"type\":\"track\",\"uri\":\"spotify:track:4CpKEkdGbOJV51cSvx7SoG\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1ozpmkWcCHwsQ4QTnxOOdT\"},\"href\":\"https://api.spotify.com/v1/albums/1ozpmkWcCHwsQ4QTnxOOdT\",\"id\":\"1ozpmkWcCHwsQ4QTnxOOdT\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/77b0c91524867cc72d1974f66ad8cd21d063a20e\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/f2405b82d0578dd815a3082ca0f7ec4e18e937a1\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/a5435bb3ab4fabe43bc7f7ce46a6c23aa30d8eae\",\"width\":64}],\"name\":\"What A Time To Be Alive\",\"type\":\"album\",\"uri\":\"spotify:album:1ozpmkWcCHwsQ4QTnxOOdT\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":205879,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500300\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/27GmP9AWRs744SzKcpJsTZ\"},\"href\":\"https://api.spotify.com/v1/tracks/27GmP9AWRs744SzKcpJsTZ\",\"id\":\"27GmP9AWRs744SzKcpJsTZ\",\"name\":\"Jumpman\",\"popularity\":77,\"preview_url\":\"https://p.scdn.co/mp3-preview/4f3e954bb232a96c196389017d961016c8cbd7fc?cid=null\",\"track_number\":9,\"type\":\"track\",\"uri\":\"spotify:track:27GmP9AWRs744SzKcpJsTZ\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":267066,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51500238\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1OAYKfE0YdrN7C1yLWaLJo\"},\"href\":\"https://api.spotify.com/v1/tracks/1OAYKfE0YdrN7C1yLWaLJo\",\"id\":\"1OAYKfE0YdrN7C1yLWaLJo\",\"name\":\"Hotline Bling\",\"popularity\":75,\"preview_url\":\"https://p.scdn.co/mp3-preview/53a8f039eb0b567e47868f5a53de4683ba5d5f0c?cid=null\",\"track_number\":20,\"type\":\"track\",\"uri\":\"spotify:track:1OAYKfE0YdrN7C1yLWaLJo\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":189853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600078\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4YJmZfvlheSziXem8HBWrj\"},\"href\":\"https://api.spotify.com/v1/tracks/4YJmZfvlheSziXem8HBWrj\",\"id\":\"4YJmZfvlheSziXem8HBWrj\",\"name\":\"Still Here\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/39384d3485d21184dd3719cfd8d644182b0b1d8b?cid=null\",\"track_number\":10,\"type\":\"track\",\"uri\":\"spotify:track:4YJmZfvlheSziXem8HBWrj\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/79qV4McLzhs8U3FyRKnocz\"},\"href\":\"https://api.spotify.com/v1/albums/79qV4McLzhs8U3FyRKnocz\",\"id\":\"79qV4McLzhs8U3FyRKnocz\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/2151a609fd5a5ec69586920a85bf308cdf56f3a1\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/9c6eb30ff5270c115b1ecd2b74430e505c281f25\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/ef4e90b4dde72134365a732659dccf9e1bd7b519\",\"width\":64}],\"name\":\"Back To Back\",\"type\":\"album\",\"uri\":\"spotify:album:79qV4McLzhs8U3FyRKnocz\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":170637,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500241\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/5lFDtgWsjRJu8fPOAyJIAK\"},\"href\":\"https://api.spotify.com/v1/tracks/5lFDtgWsjRJu8fPOAyJIAK\",\"id\":\"5lFDtgWsjRJu8fPOAyJIAK\",\"name\":\"Back To Back\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/b5bb11586af5cfde7c0eaef26300b2f6f62d2ac4?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:5lFDtgWsjRJu8fPOAyJIAK\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0ptlfJfwGTy0Yvrk14JK1I\"},\"href\":\"https://api.spotify.com/v1/albums/0ptlfJfwGTy0Yvrk14JK1I\",\"id\":\"0ptlfJfwGTy0Yvrk14JK1I\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/d329671363eb7826b5871eef978841c7db97c757\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/bcd6801c26cb293a45df9b092227395c5b403b4c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/14d65d4565838431345e35575b8b74d95134990a\",\"width\":64}],\"name\":\"If You're Reading This It's Too Late\",\"type\":\"album\",\"uri\":\"spotify:album:0ptlfJfwGTy0Yvrk14JK1I\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":241853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500010\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1ID1QFSNNxi0hiZCNcwjUC\"},\"href\":\"https://api.spotify.com/v1/tracks/1ID1QFSNNxi0hiZCNcwjUC\",\"id\":\"1ID1QFSNNxi0hiZCNcwjUC\",\"name\":\"Legend\",\"popularity\":72,\"preview_url\":\"https://p.scdn.co/mp3-preview/34fe00d7d951e42017bbbd8a424244c3cf1006e1?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:1ID1QFSNNxi0hiZCNcwjUC\"}]}")

# 1. How many songs are there?
# What is data?
print(type(data))

# Oh, a dictionary. Let's look at the keys.
print(data.keys())

print(data['tracks'])

# Okay, that's a list of songs. How many?
print("There are", len(data['tracks']), "songs")

# 2. List the name of each song, along with its popularity.

# I'm going to be doing a lot of stuff with these songs,
# so I'm going to save them into a variable name that makes sense
# I don't *have to*, but it will read nicer
songs = data['tracks']

# What kind of keys do I have to work with?
# I'll look at the keys of the first song to find out.
print(songs[0].keys())

# Okay, I'll loop through and print out name and popularity
for song in songs:
  print(song['name'], "has a popularity of", song['popularity'])

# 3. How long would it take, in minutes, to listen to all of these songs in a row?

# VERSION ONE:
# Loop through and keep adding each song's duration to my total
total_duration_ms = 0
for song in songs:
  total_duration_ms = total_duration_ms + song['duration_ms']

# VERSION TWO: 
# Use a list comprehension (!!??!?!?) to take the list of 
# songs and turn it into a list of duration_ms 
# then use sum() to add them together
durations = [song['duration_ms'] for song in songs]
duration_ms = sum(durations)

# 1000ms in a second
# 60 seconds in a minute
duration_min = total_duration_ms / 1000 / 60
duration_min = round(duration_min, 2)
print("It would take", duration_min, "minutes")

# 4. For each song, list every artist that worked on it.
# VERSION ONE
for song in songs:
  print("Song name:", song['name'])
  for artist in song['artists']:
    print("  -", artist['name'])

# VERSION TWO: Use a loop to build a new list
for song in songs:
  names = []
  for artist in song['artists']:
    names.append(artist['name'])
  # We now have a list that looks like ['Drake', 'WizKid', 'Kyla']
  # we will use .join to turn it into 'Drake and WizKid and Kyle'
  names_sentence = ' and '.join(names)
  print(song['name'], "was made by", names_sentence)

# VERSION THREE: Use a list compehension to create a new list of names
# It's the same as what we did for VERSION TWO, almost
for song in songs:
  names = [artist['name'] for artist in song['artists']]
  names_sentence = ' and '.join(names)
  print(song['name'], "was made by", names_sentence)

# 5. For each song, list every musician that worked on it EXCEPT drake
# This is terrible when Drake is the only musician on it
# but I didn't tell you to make it nice in that situation so we can just suffer

# VERSION ONE: Same as version one above, just with an if statement
for song in songs:
  print("Song name:", song['name'])
  for artist in song['artists']:
    if artist['name'] != 'Drake':
      print("  -", artist['name'])

# VERSION TWO: Same as version three above, just with an if statement
# inside of the list comprehension to only give non-Drake artists

for song in songs:
  names = [artist['name'] for artist in song['artists'] if artist['name'] != 'Drake']
  names_sentence = ' and '.join(names)
  print(song['name'], "was made by", names_sentence)

# 6. How many songs are from albums, and how many are from singles?

# VERSION ONE: Use a counter with an if statement
album_count = 0
single_count = 0
for song in songs:
  if song['album']['album_type'] == 'album':
    album_count = album_count + 1
  elif song['album']['album_type'] == 'single':
    single_count = single_count + 1

print("There were", album_count, "from albums")
print("There were", single_count, "from singles")

# VERSION TWO: Use a list comprehension to build two new lists -
# one of songs from albums, one of songs from singles
# then we'll use len to see how long they are

album_songs = [song for song in songs if song['album']['album_type'] == 'album']
single_songs = [song for song in songs if song['album']['album_type'] == 'single']

print("There were", len(album_songs), "from albums")
print("There were", len(single_songs), "from singles")

# 7. What percentage of these songs are marked as explicit?

# VERSION ONE: Use a for loop, same as above
# 'explicit' is True/False, so we don't need to do a == True
explicit_count = 0
for song in songs:
  if song['explicit']:
    explicit_count = explicit_count + 1

print(explicit_count, "songs were explicit")

# VERSION TWO: list comprehension

explicit_songs = [song for song in songs if song['explicit']]
print(len(explicit_songs), "songs were explicit")

# 8. I'd like to listen to one of the songs! Is there maybe a URL where I can listen to it?

# Depends on what we're talking about, but either of these will work

print(songs[0]['preview_url'])
print(songs[0]['href'])

# 9. What is the most popular song?
# There are a million billion ways to do this.
# VERSION ONE: They're already in order of popularity

print(songs[0]['name'])

# VERSION TWO: Use a lambda to sort the list by a key

sorted_songs = sorted(songs, key=lambda song: song['popularity']) 
most_popular = sorted_songs[-1]
print("The most popular song is", most_popular['name'])

# VERSION THREE: Keep track of the most popular in a loop with two variables
# When you find one with a higher popularity than the highest you've seen
# so far, save it into these variables
most_popular_popularity = 0
most_popular_title = ''

for song in songs:
  if song['popularity'] > most_popular_popularity:
    most_popular_popularity = song['popularity']
    most_popular_title = song['name']

print("The most popular song is", most_popular_title, "with a score of", most_popular_popularity)

# VERSION FOUR: Keep track of the most popular in a single variable,
# just a copy of the song dictionary

most_popular = {
  'name': 'NOTHING!!!',
  'popularity': 0
}

for song in songs:
  if song['popularity'] > most_popular['popularity']:
    most_popular = song

print("The most popular is", most_popular['name'], "with a popularity of", most_popular['popularity'])

# VERSION FIVE: Find the highest popularity score
# then loop through and print the song matching that
# This works well for ties since multiple answers can be printed

highest_popularity = 0

# First loop through to find the highest popularity
for song in songs:
  if song['popularity'] > highest_popularity:
    highest_popularity = song['popularity']

# Then loop through to print the songs with that popularity
for song in songs:
  if song['popularity'] == highest_popularity:
    print(song['name'], "is the most popular song")


# VERSION SIX: List comprehension version of above
# Make a list of just popularities
popularities = [song['popularity'] for song in songs]
# Pull out the maximum from that list
max_popularity = max(popularities)
# Go through the songs printing out the ones that match
for song in songs:
  if song['popularity'] == max_popularity:
    print(song['name'], "is the most popular song")

