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

# Contributing
NyaaRequest was made out of boredom and the need to learn python. I was tired of learning through tutorials so i thought that doing projects would be the best way. So contributing is very helpful for me to learn good python practices. 

**Any kind of contributions, from issues to PRs, help. Thank you.**