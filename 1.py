import json

def biodata(namaInput, umurInput):
    biodatadict = {
        "name" : namaInput,
        "age" : umurInput,
        "address" : "Jl. Garegea No. 29",
        "hobbies" : ["Baca Manga","Nonton Anime"],
        "is_married" : False,
        "list_school" : {
            "SD":{
                "name" : 'SD Teladan Merpati',
                "year_in" : 2002,
                "year_out" : 2008,
                "major" : None
            },
            "SMP":{
                "name" : 'SMP Negeri 1 Bantaeng',
                "year_in" : 2008,
                "year_out" : 2011,
                "major" : None
            },
            "SMA":{
                "name" : 'SMA 1 Bantaeng',
                "year_in" : 2011,
                "year_out" : 2014,
                "major" : "IPA"
            },
            "Perguruan Tinggi":{
                "name" : 'Politeknik Negeri Ujung Pandang',
                "year_in" : 2014,
                "year_out" : 2018,
                "major" : "Teknik Multimedia dan Jaringan"
            }
        },
        "skills" : {
            "1" : {
                "name_skill" : "python",
                "level" : "advanced"
            },
            "2" : {
                "name_skill" : "java",
                "level" : "beginner"
            },
        },
        "interest_in_coding" : True
    }
    
    app_json = json.dumps(biodatadict)
    
    return app_json

biodataAmal = biodata("Amal", 23)

print(biodataAmal)