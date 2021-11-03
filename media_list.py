#! /usr/bin/env python3
# coding=utf-8

# Author: Ruibo Liu (ruibo.liu.gr@dartmoputh.edu)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from enum import Enum


# SET THE MEDIAS OF YOUR INTERESTS HERE !!!
# class Media(Enum):
#     # # Liberal
#     # BBC = 1094
#     # CNN = 1095
#     # NYT = 1
#     # NPR = 1096
#     # WSP = 2
#     # HUFF = 27502
#     # GDN = 18629

#     # # Neutral
#     # CNBC = 1755
#     # USA = 4
#     # WSJ = 1150
#     # CBS = 1752
#     # ABC = 1091

#     # # Conservative
#     # BLZ = 232790
#     # RLS = 24669
#     # SEA = 28136
#     # FOX = 1092
#     # BRB = 19334

#     # Australia - ABC
#     ABC = 20775

#     # UK - BBC
#     BBC = 1094

#     # Canada - Big News Network - Canada
#     BNNC =  655202

#     # India - Times of India
#     TOI = 39784

#     # USA - New York Times, Fox, Wall Street Journal
#     NYT = 1
#     FOX = 1092
#     WSJ = 1150

ABBREVIATIONS = {
    "ABC": "ABC",
    "Big News Network - Canada": "BNNC",
}

# ==== INTERNATIONAL DATA ====
class InternationalMediaIds(Enum):
    # Australia - Sydney Morning Herald
    SMH = 19320

    # UK - BBC
    BBC = 1094

    # Canada - Big News Network - Canada
    BNNC =  655202

    # India - Times of India
    TOI = 39784

    # USA - New York Times, Fox, Wall Street Journal
    NYT = 1
    FOX = 1092
    WSJ = 1150

INTL_MEDIA_BY_PLACE = { "AUS": ["SMH"], "UK": ["BBC"], "CAN": ["BNNC"], "IND": ["TOI"], "USA": ["NYT", "FOX", "WSJ"] }
INTL_PLACE_FROM_MEDIA = { "SMH": "AUS", "BBC": "UK", "BNNC": "CAN", "TOI": "IND", "NYT": "USA", "FOX": "USA", "WSJ": "USA"}
INTL_PLACE_FROM_MEDIA_ID = { InternationalMediaIds.SMH.value: "AUS", InternationalMediaIds.BBC.value: "UK", InternationalMediaIds.BNNC.value: "CAN", InternationalMediaIds.TOI.value: "IND", InternationalMediaIds.NYT.value: "USA", InternationalMediaIds.FOX.value: "USA", InternationalMediaIds.WSJ.value: "USA"}

InternationalMedia = { "MediaToIds": InternationalMediaIds, "MediaByPlace": INTL_MEDIA_BY_PLACE, "PlaceFromMedia": INTL_PLACE_FROM_MEDIA, "PlaceFromMediaId": INTL_PLACE_FROM_MEDIA_ID}


# ==== DOMESTIC DATA ====
class DomesticMediaIds(Enum):
    # NY - New York Daily News
    NYDN = 269292

    # CA - LA Times
    LAT = 6

    # TX - Focus Daily News
    FDN = 1168

    # GA - Atlanta Tribune
    AT = 104293

US_MEDIA_BY_PLACE = { "NY": ["NYDN"], "CA": "LAT", "TX": "FDN", "GA": "AT"}
US_PLACE_FROM_MEDIA = { "NYDN": "NY", "LAT": "CA", "FDN": "TX", "AT": "GA"}
US_PLACE_FROM_MEDIA_ID = { DomesticMediaIds.NYDN.value: "NY", DomesticMediaIds.LAT.value: "CA", DomesticMediaIds.FDN.value: "TX", DomesticMediaIds.AT.value: "GA"}

DomesticMedia = {"MediaToIds": DomesticMediaIds, "MediaByPlace": US_MEDIA_BY_PLACE, "PlaceFromMedia": US_PLACE_FROM_MEDIA, "PlaceFromMediaId": US_PLACE_FROM_MEDIA_ID}

# === COMBINED ====
Media = { "INTL": InternationalMedia, "US": DomesticMedia }