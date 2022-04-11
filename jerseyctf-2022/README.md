# Write-ups

## Bin

|    Challenge     | Write-ups                    |
| :--------------: | :--------------------------- |
|    block-game    | [writeups](block-game)       |
|  context-clues   | [writeups](context-clues)    |
|    going_over    | [writeups](going_over)       |
|     kangaroo     | [writeups](kangaroo)         |
|   misdirection   | [writeups](misdirection)     |
|     patches      | [writeups](patches)          |
|    symbolism     | [writeups](symbolism)        |
| win-bin-analysis | [writeups](win-bin-analysis) |

### Crypto 

|       Challenge       | Write-ups                         |
| :-------------------: | :-------------------------------- |
|  audio-transmission   | [writeups](audio-transmission)    |
|   file-zip-cracker    | [writeups](file-zip-cracker)      |
| hidden-in-plain-sight | [writeups](hidden-in-plain-sight) |
|    inDEStructible     | [writeups](inDEStructible)        |
|     new-algorithm     | [writeups](new-algorithm)         |
|         salad         | [writeups](salad)                 |
|    secret-message     | [writeups](secret-message)        |
|   would-you-wordle    | [writeups](would-you-wordle)      |
|        xoracle        | [writeups](xoracle)               |


### Forensics

|   Challenge    | Write-up                   |
| :------------: | :------------------------- |
| corrupted-file | [writeups](corrupted-file) |
|  data-backup   | [writeups](data-backup)    |
|    infected    | [writeups](infected)       |
| recent-memory  | [writeups](recent-memory)  |
| scavenger-hunt | [writeups](scavenger-hunt) |
| speedy-at-midi | [writeups](speedy-at-midi) |
|  stolen-data   | [writeups](stolen-data)    |

## Misc

|     Challenge      | Write-ups                      |
| :----------------: | :----------------------------- |
|    bank-clients    | [writeups](bank-clients)       |
| check-the-shadows  | [writeups](check-the-shadows)  |
| dnsmasq-ip-extract | [writeups](dnsmasq-ip-extract) |
|  filtered-feeders  | [writeups](filtered-feeders)   |
|   firewall-rules   | [writeups](firewall-rules)     |
|      root-me       | [writeups](root-me)            |
|     snort-log      | [writeups](snort-log)          |
|      we-will       | [writeups](we-will)            |


## OSINT

|     Challenge      | Write-ups                      |
| :----------------: | :----------------------------- |
|    contributor     | [writeups](contributor)        |
|      dns-joke      | [writeups](dns-joke)           |
|      mystery       | [writeups](mystery)            |
|   photo-op-spot    | [writeups](photo-op-spot)      |
|       rarity       | [writeups](rarity)             |
| sho-me-whats-wrong | [writeups](sho-me-whats-wrong) |


## Web

|     Challenge     | Write-ups                     |
| :---------------: | :---------------------------- |
|    apache-logs    | [writeups](apache-logs)       |
|      buster       | [writeups](buster)            |
|  cookie-factory   | [writeups](cookie-factory)    |
|    flag-vault     | [writeups](flag-vault)        |
| heres-my-password | [writeups](heres-my-password) |
|  road-not-taken   | [writeups](road-not-taken)    |
| seigwards-secrets | [writeups](seigwards-secrets) |


<!-- 
Works in Bash

# Get Challenge Names in Directories and outputs them to file
ls ../{CATEGORY} -l | grep '^d' | awk '{print $9}' | sed 's/.$//' > {CATEGORY}

ex. 
ls ../forensics/ -l | awk '{print $9}' | sed 's/.$//' > forensics

-----

# Get writeup format by category
category={CATEGORY}; while read -r chal; do printf "| [$chal](../$category/$chal) | [writeups]($chal)\n"; done < $category

ex.
category=bin; while read -r chal; do printf "| [$chal](../$category/$chal) | [writeups]($chal)\n"; done < $category

---

# make directory for all challenges
mkdir `cat bin crypto forensics misc osint web`

# add .keep file to all challenges
for dir in `ls -l | grep '^d' | awk '{print $9}'`; do cd $dir; touch .keep; cd ..; done

--> 
