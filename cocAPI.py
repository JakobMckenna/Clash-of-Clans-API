# Still need to add more error checking
# To run: python3.11 -u "/Users/jakobmckenna/Desktop/Projects/cocAPI.py"
import requests

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjljYTkwMzU5LTkwMzAtNDkwYy05YTFkLTFmNDExMjdlMzk0MSIsImlhdCI6MTY4Mzg0NzczNSwic3ViIjoiZGV2ZWxvcGVyLzNhYWVlOTUzLTllNmUtN2MzMy02NGMzLWM2MjI4NTExNGFlZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjI0Ljc3LjE1MS4xMDMiXSwidHlwZSI6ImNsaWVudCJ9XX0.6r6bKkIh8RYrpfggSBIbQlQ5TCQxhE8D8rA2GMGGSLA_BQ4051wedSXtUv0BT7Xq2da_OA58LCfHxVjWWlOksg',
    'Accept': 'application/json'
}

def getCWL():
    part1 = "https://api.clashofclans.com/v1/clans/%23"
    part2 = input1
    part2 = part2.replace("#", "")
    part3 = "/currentwar/leaguegroup"
    newStr = part1 + part2 + part3

    
    try:
        response = requests.get(
            newStr, headers=headers)
        CWL_json = response.json()
        print("Analyzing CWL war results")
        
        if(str(CWL_json) == "{'reason': 'notFound'}"):
            print("Clan info not found...")
            print("\n End of program")
            return
        
        print("\nCWL season date: " + CWL_json['season'])

        i = 0
        totalStars = 0
        totalAttacks = 0
        for warTags in CWL_json['rounds']:
            i+=1
            print("\nRound " + str(i) + " tags: " + str(warTags['warTags']) + "\n")

        
            strHolder = str(warTags['warTags'])
            strHolder = strHolder.replace("[", "")
            strHolder = strHolder.replace("#", "")
            strHolder = strHolder.replace("'", "")
            strHolder = strHolder.replace("]", "")
            strHolder = strHolder.replace(" ", "")
            tagList = strHolder.split(",")

            missedAttacks = "Missed Attacks:\n" 
        
            for x in range(len(tagList)):
                warTagHolder = "https://api.clashofclans.com/v1/clanwarleagues/wars/%23" + tagList[x]
        
                response2 = requests.get(
                    warTagHolder, headers=headers)
                CWLWar_json = response2.json()

                if str(CWLWar_json['clan']['tag']) == input1:
                    print("Clan name    : " + str(CWLWar_json['clan']['name']))
                    print("Attacks      : " + str(CWLWar_json['clan']['attacks']))
                    print("Stars        : " + str(CWLWar_json['clan']['stars']))
                    print("Clan name 2  : " + str(CWLWar_json['opponent']['name']))
                    print("Attacks      : " + str(CWLWar_json['opponent']['attacks']))
                    print("Stars        : " + str(CWLWar_json['opponent']['stars']))

                    totalStars += CWLWar_json['clan']['stars']
                    totalAttacks += CWLWar_json['clan']['attacks']

                    #if(CWLWar_json['clan']['tag']['attacks']['stars'] != ""):
                        #missedAttacks += str(CWLWar_json['clan']['members'][2]) 
                        #missedAttacks += ", "  
                         
                if str(CWLWar_json['opponent']['tag']) == input1: 
                    print("Clan name    : " + str(CWLWar_json['opponent']['name']))
                    print("Attacks      : " + str(CWLWar_json['opponent']['attacks']))
                    print("Stars        : " + str(CWLWar_json['opponent']['stars']))
                    print("Clan name 2  : " + str(CWLWar_json['clan']['name']))
                    print("Attacks      : " + str(CWLWar_json['clan']['attacks']))
                    print("Stars        : " + str(CWLWar_json['clan']['stars']))

                    totalStars += CWLWar_json['opponent']['stars']
                    totalAttacks += CWLWar_json['opponent']['attacks']

 
        avgStars = totalStars/totalAttacks
        avgStars = round(avgStars, 3)
        numAttacks = 15*7
        missingAttacks = numAttacks - totalAttacks
        print("\nOverall stats: ")
        print("Total stars:        " + str(totalStars))
        print("Total attacks:      " + str(totalAttacks))
        print("Average stars:      " + str(avgStars))
        print("Missed attacks:     " + str(missingAttacks))
        print(missedAttacks)

        print("\nEnd of program")
    except requests.exceptions.RequestException:
        print("\nERROR IN CLAN TAG PROVIDED: please try again \n")

input1 = input("Enter a clan tag (Ex: #29PR98): ")
if(input1.find('#') != -1):
    print("Searching clan tag...")
else:
    print("\nMake sure your clan tag contains a #")
    input1 = input("Enter a clan tag: ")
print("Searching for clan: " + input1)

# Call the function
getCWL()