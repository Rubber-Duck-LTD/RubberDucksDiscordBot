import json, urllib  # For reference, importing.


one_country_object = {
    "Country": "Afghanistan",
    "CountryCode": "AF",
    "Slug": "afghanistan",
    "NewConfirmed": 44,
    "TotalConfirmed": 39341,
    "NewDeaths": 0,
    "TotalDeaths": 1462,
    "NewRecovered": 10,
    "TotalRecovered": 32852,
    "Date": "2020-10-06T02:49:09Z",
    "Premium": {}
}


two_countries_list_of_dicts = [{
    "Country": "Afghanistan",
    "CountryCode": "AF",
    "Slug": "afghanistan",
    "NewConfirmed": 44,
    "TotalConfirmed": 39341,
    "NewDeaths": 0,
    "TotalDeaths": 1462,
    "NewRecovered": 10,
    "TotalRecovered": 32852,
    "Date": "2020-10-06T02:49:09Z",
    "Premium": {}
}, {
    "Country": "Finland",
    "CountryCode": "FI",
    "Slug": "finland",
    "NewConfirmed": 40,
    "TotalConfirmed": 200,
    "NewDeaths": 3,
    "TotalDeaths": 1200,
    "NewRecovered": 100,
    "TotalRecovered": 2000,
    "Date": "2020-11-06T02:49:09Z",
    "Premium": {}
}]

five_countries_list_of_dicts = [{
    "Country": "Algeria",
    "CountryCode": "DZ",
    "Slug": "algeria",
    "NewConfirmed": 844,
    "TotalConfirmed": 66819,
    "NewDeaths": 15,
    "TotalDeaths": 2139,
    "NewRecovered": 420,
    "TotalRecovered": 44199,
    "Date": "2020-11-15T17:25:38Z",
    "Premium": {}
},
    {
    "Country": "Andorra",
    "CountryCode": "AD",
    "Slug": "andorra",
    "NewConfirmed": 0,
    "TotalConfirmed": 5725,
    "NewDeaths": 0,
    "TotalDeaths": 75,
    "NewRecovered": 0,
    "TotalRecovered": 4675,
    "Date": "2020-11-15T17:25:38Z",
    "Premium": {}
},
    {
    "Country": "Angola",
    "CountryCode": "AO",
    "Slug": "angola",
    "NewConfirmed": 146,
    "TotalConfirmed": 13374,
    "NewDeaths": 5,
    "TotalDeaths": 322,
    "NewRecovered": 19,
    "TotalRecovered": 6345,
    "Date": "2020-11-15T17:25:38Z",
    "Premium": {}
},
    {
    "Country": "Antigua and Barbuda",
    "CountryCode": "AG",
    "Slug": "antigua-and-barbuda",
    "NewConfirmed": 1,
    "TotalConfirmed": 134,
    "NewDeaths": 1,
    "TotalDeaths": 4,
    "NewRecovered": 3,
    "TotalRecovered": 127,
    "Date": "2020-11-15T17:25:38Z",
    "Premium": {}
},
    {
    "Country": "Argentina",
    "CountryCode": "AR",
    "Slug": "argentina",
    "NewConfirmed": 8468,
    "TotalConfirmed": 1304846,
    "NewDeaths": 262,
    "TotalDeaths": 35307,
    "NewRecovered": 8889,
    "TotalRecovered": 1119366,
    "Date": "2020-11-15T17:25:38Z",
    "Premium": {}
}]


own_coordinate_location_mockup = {
    "info": {
        "statuscode": 0,
        "copyright": {
            "text": "© 2020 MapQuest, Inc.",
            "imageUrl": "http://api.mqcdn.com/res/mqlogo.gif",
            "imageAltText": "© 2020 MapQuest, Inc."
        },
        "messages": []
    },
    "options": {
        "maxResults": -1,
        "thumbMaps": "false",
        "ignoreLatLngInput": "false"
    },
    "results": [
        {
            "providedLocation": {
                "location": "Marsinkuja 1, Finland"
            },
            "locations": [
                {
                    "street": "Marsinkuja 1",
                    "adminArea6": "",
                    "adminArea6Type": "Neighborhood",
                    "adminArea5": "Vantaa",
                    "adminArea5Type": "City",
                    "adminArea4": "",
                    "adminArea4Type": "County",
                    "adminArea3": "Uusimaa",
                    "adminArea3Type": "State",
                    "adminArea1": "FI",
                    "adminArea1Type": "Country",
                    "postalCode": "01480",
                    "geocodeQualityCode": "P1ACA",
                    "geocodeQuality": "POINT",
                    "dragPoint": "false",
                    "sideOfStreet": "N",
                    "linkId": "FI/PAD/p0/938289",
                    "unknownInput": "",
                    "type": "s",
                    "latLng": {
                        "lat": 60.34115,
                        "lng": 25.09898
                    },
                    "displayLatLng": {
                        "lat": 60.34115,
                        "lng": 25.09898
                    }
                }
            ]
        }
    ]
}


mock_up_response_for_stops = { # Checking example responses from HSL. Another 
  "data": {
    "nearest": {
      "edges": [
        {
          "node": {
            "place": {
              "lat": 60.20298,
              "lon": 24.93323,
              "name": "Vaihdemiehenkatu",
              "gtfsId": "HSL:1173107",
              "code": "H2183",
              "routes": [
                {
                  "id": "Um91dGU6SFNMOjE1MDY=",
                  "shortName": "506"
                },
                {
                  "id": "Um91dGU6SFNMOjc4NDg=",
                  "shortName": "848"
                },
                {
                  "id": "Um91dGU6SFNMOjEwNjk=",
                  "shortName": "69"
                }
              ]
            },
            "distance": 192
          }
        },
        {
          "node": {
            "place": {
              "lat": 60.19989,
              "lon": 24.93402,
              "name": "Pasilan asema",
              "gtfsId": "HSL:1173106",
              "code": "H0620",
              "routes": [
                {
                  "id": "Um91dGU6SFNMOjEwNjk=",
                  "shortName": "69"
                },
                {
                  "id": "Um91dGU6SFNMOjE1MDY=",
                  "shortName": "506"
                },
                {
                  "id": "Um91dGU6SFNMOjc4NDg=",
                  "shortName": "848"
                }
              ]
            },
            "distance": 238
          }
        },
        {
          "node": {
            "place": {
              "lat": 60.2026,
              "lon": 24.9329,
              "name": "Vaihdemiehenkatu",
              "gtfsId": "HSL:1173108",
              "code": "H2184",
              "routes": [
                {
                  "id": "Um91dGU6SFNMOjEwNjk=",
                  "shortName": "69"
                },
                {
                  "id": "Um91dGU6SFNMOjE1MDY=",
                  "shortName": "506"
                },
                {
                  "id": "Um91dGU6SFNMOjc4NDg=",
                  "shortName": "848"
                }
              ]
            },
            "distance": 247
          }
        },
        {
          "node": {
            "place": {
              "lat": 60.20141,
              "lon": 24.93678,
              "name": "Messukeskus",
              "gtfsId": "HSL:1173433",
              "code": "H0614",
              "routes": [
                {
                  "id": "Um91dGU6SFNMOjEwMDI=",
                  "shortName": "2"
                },
                {
                  "id": "Um91dGU6SFNMOjEwMDk=",
                  "shortName": "9"
                },
                {
                  "id": "Um91dGU6SFNMOjEwMDc=",
                  "shortName": "7"
                }
              ]
            },
            "distance": 260
          }
        },
        {
          "node": {
            "place": {
              "lat": 60.19951,
              "lon": 24.93424,
              "name": "Pasilan asema",
              "gtfsId": "HSL:1220434",
              "code": "H0612",
              "routes": [
                {
                  "id": "Um91dGU6SFNMOjEwMDk=",
                  "shortName": "9"
                }
              ]
            },
            "distance": 284
          }
        },
        {
          "node": {
            "place": {
              "lat": 60.19942,
              "lon": 24.93461,
              "name": "Pasilan asema",
              "gtfsId": "HSL:1173105",
              "code": "H2367",
              "routes": [
                {
                  "id": "Um91dGU6SFNMOjE1MDY=",
                  "shortName": "506"
                },
                {
                  "id": "Um91dGU6SFNMOjc4NDg=",
                  "shortName": "848"
                },
                {
                  "id": "Um91dGU6SFNMOjEwNjk=",
                  "shortName": "69"
                }
              ]
            },
            "distance": 308
          }
        }
      ]
    }
  }
}


def fetch_food(): # Simulating how this fetch works. Testing the desired effect.
    url = "https://foodandco.fi/modules/json/json/Index?costNumber=0083&language=fi"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        data = json.loads(html)
        menu = data["MenusForDays"]
        return menu


test_origin_destination_data = {
  "data": {
    "plan": {
      "itineraries": [
        {
          "walkDistance": 649.102153853899,
          "duration": 2096,
          "legs": [
            {
              "mode": "WALK",
              "startTime": 1605477642000,
              "endTime": 1605477900000,
              "from": {
                "lat": 60.168992,
                "lon": 24.932366,
                "name": "Kamppi, Helsinki",
                "stop": "null"
              },
              "to": {
                "lat": 60.16895,
                "lon": 24.93146,
                "name": "Kamppi",
                "bikePark": "null",
                "stop": {
                  "code": "H1248",
                  "name": "Kamppi",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "agency": "null",
              "distance": 164.119,
              "legGeometry": {
                "length": 19,
                "points": "ewfnJgrdwC[qAS}@W`@????@ONWb@jBDNDP@FBHDPBJ@DBNDPIN"
              }
            },
            {
              "mode": "BUS",
              "startTime": 1605477900000,
              "endTime": 1605479340000,
              "from": {
                "lat": 60.16895,
                "lon": 24.93146,
                "name": "Kamppi",
                "stop": {
                  "code": "H1248",
                  "name": "Kamppi",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "to": {
                "lat": 60.17298,
                "lon": 24.6873,
                "name": "Puolarmetsänkatu",
                "bikePark": "null",
                "stop": {
                  "code": "E4324",
                  "name": "Puolarmetsänkatu",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "agency": {
                "gtfsId": "HSL:HSL",
                "name": "Helsingin seudun liikenne"
              },
              "distance": 16072.325697226042,
              "legGeometry": {
                "length": 301,
                "points": "}vfnJsldwC{@eBMx@f@vBd@nBFTtA|FhBlGdEpB`CbATFt@\\j@XpAf@p@zCJtAd@zL^zI?pAZtb@HdJBtC}C|Bg@v@a@x@_@n@Mb@qAxD_@vASfAObAa@jDe@rF]~FMdEEjCAt@B~FB~BF~CV~G`JfbBRvCR~Cr@xIfA|LP`BZ`DvBtQ`@lDnAbKt@bHNlBTrDHfCHtFCpGOvFMfCk@vG}BdUc@nEg@nFOxAk@|Fc@lE_@|De@pEg@hFwAxNu@rHIl@c@xDk@lFE^SbB[nCMfAwAjKqCtOcA`Hu@vGe@tDe@zEoAfNc@pDu@lHW`DUlCMjBOnCA^C\\G~ACt@AT?p@C|@@fBGpFAdF?rFKjSA|GOzPHPcDl@o@DaERsBF}@Cu@AkAHcCTm@J{@VeA\\{Al@EQKUQOWG_@FUJe@PMx@Iz@?p@Dj@Hb@LTZT`@@LGZJVPP`@P|@PtBJ~BTvDhC`\\NjEB|AMtFBbAJtA^rBfBrLPxATdCNlDFnCKtCBj@KjIAfCAhDGtLD|@D|AF`AN~AXbCl@`DdD|Rh@fEbBhI\\dCb@nGN|DFhF@dCCvCQnFGbPB`Ed@hLE~Eh@vJd@h]FjBLfCXdChApLJ|Gn@vLFzBuAx@mBhAwAvAo@v@_BzAa@^w@j@{@f@wAnAIFmCjBcBxAcBlBgA~Aa@p@d@hCFf@Lx@Lf@Hf@H`CFjDDvD@p@Cj@GjAGt@CHKpBA`CB|AVrHHrC@PN|DVbHHdDTxFdAOv@[t@m@\\Sb@rBZ|A\\`CLx@VxGN`E@r@J`CHpBJdCBf@Bb@BfAY?Q@i@H{@RuCr@w@\\YXY`@_ApB}AdG_@v@Yb@iCvCg@bAk@lBUrBG~A?j@Ab@BjAPxBb@lDj@tDjBzJJj@DPhAfFdA`IVvBLpATvCRlCPrETfI@`C@lDAxAU|RAlAB|BF|BD`AFfAPhCLpARdBRbARnAXrA^fBPnARzAJpA`@nIDdBH|BFjBEjB"
              }
            },
            {
              "mode": "WALK",
              "startTime": 1605479340000,
              "endTime": 1605479738000,
              "from": {
                "lat": 60.17298,
                "lon": 24.6873,
                "name": "Puolarmetsänkatu",
                "stop": {
                  "code": "E4324",
                  "name": "Puolarmetsänkatu",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "to": {
                "lat": 60.175294,
                "lon": 24.684855,
                "name": "Pisa, Espoo",
                "bikePark": "null",
                "stop": "null"
              },
              "agency": "null",
              "distance": 484.77200000000005,
              "legGeometry": {
                "length": 29,
                "points": "gpgnJmwtuCBo@@_@CgAMiBGMKK{ABUBq@NgB~@w@l@QR@VEV]l@a@z@@VBr@@HQLITGT?T@RNt@VvALz@Jv@"
              }
            }
          ],
          "waitingTime": 0,
          "fares": [
            {
              "components": [
                {
                  "fareId": "HSL:ABC",
                  "cents": 410,
                  "currency": "EUR"
                }
              ]
            }
          ]
        },
        {
          "walkDistance": 486.20461539505504,
          "duration": 1840,
          "legs": [
            {
              "mode": "WALK",
              "startTime": 1605478657000,
              "endTime": 1605478920000,
              "from": {
                "lat": 60.168992,
                "lon": 24.932366,
                "name": "Kamppi, Helsinki",
                "stop": "null"
              },
              "to": {
                "lat": 60.16892,
                "lon": 24.93137,
                "name": "Kamppi",
                "bikePark": "null",
                "stop": {
                  "code": "H1249",
                  "name": "Kamppi",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "agency": "null",
              "distance": 169.931,
              "legGeometry": {
                "length": 20,
                "points": "ewfnJgrdwC[qAS}@W`@????@ONWb@jBDNDP@FBHDPBJ@DBNDPDPIL"
              }
            },
            {
              "mode": "BUS",
              "startTime": 1605478920000,
              "endTime": 1605480240000,
              "from": {
                "lat": 60.16892,
                "lon": 24.93137,
                "name": "Kamppi",
                "stop": {
                  "code": "H1249",
                  "name": "Kamppi",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "to": {
                "lat": 60.17571,
                "lon": 24.6874,
                "name": "Puolarmäki",
                "bikePark": "null",
                "stop": {
                  "code": "E4325",
                  "name": "Puolarmäki",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "agency": {
                "gtfsId": "HSL:HSL",
                "name": "Helsingin seudun liikenne"
              },
              "distance": 15721.620183988945,
              "legGeometry": {
                "length": 275,
                "points": "wvfnJaldwCaAwBMx@f@vBd@nBFTtA|FhBlGdEpB`CbATFt@\\j@XpAf@p@zCJtAd@zL^zI?pAZtb@HdJBtC}C|Bg@v@a@x@_@n@Mb@qAxD_@vASfAObAa@jDe@rF]~FMdEEjCAt@B~FB~BF~CV~G`JfbBRvCR~Cr@xIfA|LP`BZ`DvBtQ`@lDnAbKt@bHNlBTrDHfCHtFCpGOvFMfCk@vG}BdUc@nEg@nFOxAk@|Fc@lE_@|De@pEg@hFwAxNu@rHIl@c@xDk@lFE^SbB[nCMfAwAjKqCtOcA`Hu@vGe@tDe@zEoAfNc@pDu@lHW`DUlCMjBOnCA^C\\G~ACt@AT?p@CrEGtGAhE@|DIjSMvBSxLI|CAjB?^?dBBbA@XBx@JtARnCJjBF`AFtAFjBHhDNjFRrCJrGTpEJlCf@jLZvIJrCH|CPdJHtJBbH@nA?bB@bF?jUDdMLpKR|JHbCRjFHnBL`]A~FKxEt@bBd@t@oAfD[l@eAdBa@l@sChDuC~Co@h@eAj@E~Eh@vJd@h]FjBLfCXdChApLJ|Gn@vLFzBNrELfBHdANxAj@pDTjATt@b@nA`BfEzBvFxBnFb@vAt@hCb@zC[d@OnA@vCF|BeAXu@^g@b@QLuAvAcCfCcAfA}@|@wBvBaD`D{A~Aw@v@iBlBcAdAuA~A}ArB_@f@b@rBZ|A\\`CLx@VxGN`E@r@J`CHpBJdCBf@Bb@BfAY?Q@i@H{@RuCr@w@\\YXY`@_ApB}AdG_@v@Yb@iCvCg@bAk@lBUrBG~A?j@Ab@BjAPxBb@lDj@tDjBzJJj@DPhAfFdA`IVvBLpATvCRlCPrETfI@`C@lDAxAU|RAlAB|BF|BD`AFfAPhCLpARdBRbARnAXrA^fBPnARzAJpA`@nIDdBy@@a@@s@HeAZ_@NkAp@kAhAkB~BW`@"
              }
            },
            {
              "mode": "WALK",
              "startTime": 1605480240000,
              "endTime": 1605480497000,
              "from": {
                "lat": 60.17571,
                "lon": 24.6874,
                "name": "Puolarmäki",
                "stop": {
                  "code": "E4325",
                  "name": "Puolarmäki",
                  "wheelchairBoarding": "NO_INFORMATION"
                }
              },
              "to": {
                "lat": 60.175294,
                "lon": 24.684855,
                "name": "Pisa, Espoo",
                "bikePark": "null",
                "stop": "null"
              },
              "agency": "null",
              "distance": 315.98900000000003,
              "legGeometry": {
                "length": 26,
                "points": "cahnJkwtuCFKDGRUDRDXp@m@BEd@u@Z]@VEV]l@a@z@@VBr@@HQLITGT?T@RNt@VvALz@Jv@"
              }
            }
          ],
          "waitingTime": 0,
          "fares": [
            {
              "components": [
                {
                  "fareId": "HSL:ABC",
                  "cents": 410,
                  "currency": "EUR"
                }
              ]
            }
          ]
        }
      ]
    }
  }
}