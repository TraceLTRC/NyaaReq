# NyaaReq

NyaaRequest is a python script that allows you to programmatically browse through the search results of [Nyaa.si](https://nyaa.si). 
NyaaRequest can be used as a module or a CLI.

# Usage
    usage: NyaaReq.py query [--flags]

    positional arguments:
    query                 String to search for in nyaa.si

    optional arguments:
    -h, --help                              show this help message and exit
    -cr [CRITERIA], --criteria [CRITERIA]   Criteria to search for
    -ct [category], --category [CATEGORY]   Categories to search in, accepts multiple arguments.
    --multi                                 Enables multithreading for faster parsing
    --verbose                               Enables verbose printing

Category and Criteria uses specific arguments for each categories. These specific arguments can be seen in [types.json](https://github.com/TraceLosu/NyaaReq/blob/master/NyaaReq/types.json). These arguments follow the same naming style as the URL of the website.

## Example
    [tracel@myPC NyaaReq]$ py NyaaReq.py "Takagi-san OVA" --multi -cr 1 -ct 1_2

    name : [Aeenald] Karakai Jouzu no Takagi-san (Seasons 1-2 + OVA) | Teasing Master Takagi-san 1st & 2nd Season + OVA [BDrip 1080p][HEVC x265 10bit][AAC][WEB-OVA]
    url : https://nyaa.si/view/1284578#comments
    category : Anime English-translated
    torrent : https://nyaa.si/download/1284578.torrent
    magnet : magnet:?xt=urn:btih:31f7db083db88192d5b3dda6c2b41d3c1df98338&dn=%5BAeenald%5D%20Karakai%20Jouzu%20no%20Takagi-san%20%28Seasons%201-2%20%2B%20OVA%29%20%7C%20Teasing%20Master%20Takagi-san%201st%20%26%202nd%20Season%20%2B%20OVA%20%5BBDrip%201080p%5D%5BHEVC%20x265%2010bit%5D%5BAAC%5D%5BWEB-OVA%5D&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce
    size : 9.2 GiB
    date : 2020-09-28 07:56
    seed : 18
    leech : 6
    downloads : 476


    name : [Asakura] Karakai Jouzu no Takagi-san S1 [BDRip 1920x1080 x265 10bit FLAC] + OVA
    url : https://nyaa.si/view/1217232#comments
    category : Anime English-translated
    torrent : https://nyaa.si/download/1217232.torrent
    magnet : magnet:?xt=urn:btih:17342fcf7216d148707afabc92ffbd48afdb9b0e&dn=%5BAsakura%5D%20Karakai%20Jouzu%20no%20Takagi-san%20S1%20%5BBDRip%201920x1080%20x265%2010bit%20FLAC%5D%20%2B%20OVA&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce
    size : 10.9 GiB
    date : 2020-02-01 15:33
    seed : 31
    leech : 6
    downloads : 1764


    name : [Abystoma] Karakai Jouzu no Takagi-san | Teasing Master Takagi-san  1-12 + OVA (BD 720p) [Dual audio]
    url : https://nyaa.si/view/1136482#comments
    category : Anime English-translated
    torrent : https://nyaa.si/download/1136482.torrent
    magnet : magnet:?xt=urn:btih:b92406af0476294f288b0fc7be951f38c1fa3cdd&dn=%5BAbystoma%5D%20Karakai%20Jouzu%20no%20Takagi-san%20%7C%20Teasing%20Master%20Takagi-san%20%201-12%20%2B%20OVA%20%28BD%20720p%29%20%5BDual%20audio%5D&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce
    size : 5.1 GiB
    date : 2019-04-18 14:37
    seed : 3
    leech : 2
    downloads : 1406


    name : [0x539] Karakai Jouzu no Takagi-san - OVA (AT-X 1440x1080 x264 AAC) [487CFE2A].mkv
    url : https://nyaa.si/view/1108332#comments
    category : Anime English-translated
    torrent : https://nyaa.si/download/1108332.torrent
    magnet : magnet:?xt=urn:btih:4b8683305086484b14510f8fe311bc0c48eb6460&dn=%5B0x539%5D%20Karakai%20Jouzu%20no%20Takagi-san%20-%20OVA%20%28AT-X%201440x1080%20x264%20AAC%29%20%5B487CFE2A%5D.mkv&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce
    size : 843.8 MiB
    date : 2019-01-09 05:03
    seed : 13
    leech : 0
    downloads : 1499


    name : [KE] Karakai Jouzu no Takagi-san OVA (1024x576)[B2677BB5].mkv
    url : https://nyaa.si/view/1075337#comments
    category : Anime English-translated
    torrent : https://nyaa.si/download/1075337.torrent
    magnet : magnet:?xt=urn:btih:a811a7aa59d33b7bd290d34e0d594566df46f723&dn=%5BKE%5D%20Karakai%20Jouzu%20no%20Takagi-san%20OVA%20%281024x576%29%5BB2677BB5%5D.mkv&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce
    size : 386.9 MiB
    date : 2018-09-14 05:13
    seed : 0
    leech : 0
    downloads : 535


    name : [Otaku-san] Karakai Jouzu no Takagi-san - OVA [576p] [English Subs]
    url : https://nyaa.si/view/1059003#comments
    category : Anime English-translated
    torrent : https://nyaa.si/download/1059003.torrent
    magnet : magnet:?xt=urn:btih:4182d1d1a731e9ad581d53a34c6c9b92a8f411e0&dn=%5BOtaku-san%5D%20Karakai%20Jouzu%20no%20Takagi-san%20-%20OVA%20%5B576p%5D%20%5BEnglish%20Subs%5D&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce
    size : 252.6 MiB
    date : 2018-07-21 17:31
    seed : 6
    leech : 0
    downloads : 1124

# Contributing
NyaaRequest was made out of boredom and the need to learn python. I was tired of learning through tutorials so i thought that doing projects would be the best way. So contributing is very helpful for me to learn good python practices. 

**Any kind of contributions, from issues to PRs, help. Thank you.**