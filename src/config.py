# -*- coding: utf-8 -*-

JDBCS = {
	'dbn': 'mysql',
	'user': 'root',
	'pw': 'mysql',
	'db': 'riped-config'
}

PREDICT_MIN = 0.7

LABELS = [
    {
        "label": "Cg",
        "children": [
            {
                "value": 0,
                "label": "Cgm",
                "describe": "Matrix-supported conglomerate"
            },
            {
                "value": 1,
                "label": "Cgc",
                "describe": "Clast-supported conglomerate"
            }
        ]
    },
    {
        "label": "S",
        "children": [
            {
                "value": 2,
                "label": "Sgx",
                "describe": "Evenly/reverse-graded, cm-scale, tabular cross-bedded\nsandstone (with possible wedge-shaped toesets and\nbimodal grain size characteristics) "
            },
            {
                "value": 3,
                "label": "Spl",
                "describe": "Distinct, mm-scale 'pin-stripe' laminated sandstone\n(with bimodal grain size characteristics)"
            },
            {
                "value": 4,
                "label": "Sm",
                "describe": "Massive sandstone"
            },
            {
                "value": 5,
                "label": "Smb",
                "describe": "Massive, cryptically bioturbated sandstone"
            },
            {
                "value": 6,
                "label": "Sx",
                "describe": "High-angle cross-stratified sandstone (typically >10°)"
            },
            {
                "value": 7,
                "label": "Sl",
                "describe": "Laminated sandstone (includes low-angle and flat\nlamination)"
            },
            {
                "value": 8,
                "label": "Sr",
                "describe": "Rippled sandstone (includes current, climbing and\nwave ripple types)"
            },
            {
                "value": 9,
                "label": "Sd",
                "describe": "Deformed sandstone (undifferentiated deformation)"
            },
            {
                "value": 10,
                "label": "Sdw",
                "describe": "Dewatered sandstone"
            },
            {
                "value": 11,
                "label": "Sds",
                "describe": "Soft-sediment deformed sandstone (includes loading,\nslumping, convolute bedding)"
            },
            {
                "value": 12,
                "label": "Sdi1(Sdi2)",
                "describe": "Irregularly bedded sandstone (1) due to salt-disruption\n(sabkha fabrics); (2) due to synaeresis and salt crystal\ndisplacement"
            },
            {
                "value": 13,
                "label": "Si",
                "describe": "Dewatered sandstone"
            },
            {
                "value": 14,
                "label": "Sb",
                "describe": "Macrobioturbated sandstone (differentiated on mud\ncontent: Sb1=clean, Sb2= mud-prone; Sb3= mud-rich)"
            }
        ]
    },
    {
        "label": "SA",
        "children": [
            {
                "value": 15,
                "label": "SAm(SAx)",
                "describe": "Argillaceous sandstones are qualified as SAm, SAx,\nSAl etc. (applicable for all sandstones above, except Sb)"
            }
        ]
    },
    {
        "label": "H",
        "children": [
            {
                "value": 16,
                "label": "Hs",
                "describe": "Sand-prone heterolithics - sand bands >1cm thick\nand > than mud content; dominated by stratified/rippled\nsand-mud alternations unless otherwise specified\n(eg. intensely bioturbated Hsb, deformed Hsd)"
            },
            {
                "value": 17,
                "label": "Hm",
                "describe": "Mud-prone heterolithics - sand bands <1cm thick\n< than mud content; dominated by stratified/rippled\nsand-mud alternations unless otherwise specified\n(eg. intensely bioturbated Hmb, deformed Hmd)"
            }
        ]
    },
    {
        "label": "MS",
        "children": [
            {
                "value": 18,
                "label": "Mm",
                "describe": "Massive mudrock"
            },
            {
                "value": 19,
                "label": "Ml",
                "describe": "Laminated mudrock"
            },
            {
                "value": 20,
                "label": "Mb",
                "describe": "Bioturbated mudrock"
            },
            {
                "value": 21,
                "label": "Md",
                "describe": "Deformed/disrupted mudrock"
            },
            {
                "value": 22,
                "label": "Mc",
                "describe": "Carbonaceous mudrock"
            }
        ]
    },
    {
        "label": "C",
        "children": [
            {
                "value": 23,
                "label": "C",
                "describe": "Coal"
            }
        ]
    },
    {
        "label": "MT",
        "children": [
            {
                "value": 24,
                "label": "M",
                "describe": "Mudstone"
            }
        ]
    },
    {
        "label": "MR",
        "children": [
            {
                "value": 25,
                "label": "MR",
                "describe": "Mudrock"
            }
        ]
    },
    {
        "label": "W",
        "children": [
            {
                "value": 26,
                "label": "W",
                "describe": "Wackestone"
            }
        ]
    },
    {
        "label": "WP",
        "children": [
            {
                "value": 27,
                "label": "WP",
                "describe": "Wacke-packstone"
            }
        ]
    },
    {
        "label": "P",
        "children": [
            {
                "value": 28,
                "label": "P",
                "describe": "Packstone"
            }
        ]
    },
    {
        "label": "PG",
        "children": [
            {
                "value": 29,
                "label": "PG",
                "describe": "Pack-grainstone"
            }
        ]
    },
    {
        "label": "G",
        "children": [
            {
                "value": 30,
                "label": "G",
                "describe": "Grainstone"
            }
        ]
    },
    {
        "label": "F",
        "children": [
            {
                "value": 31,
                "label": "F",
                "describe": "Floatstone"
            }
        ]
    },
    {
        "label": "R",
        "children": [
            {
                "value": 32,
                "label": "R",
                "describe": "Rudstone"
            }
        ]
    },
    {
        "label": "B",
        "children": [
            {
                "value": 33,
                "label": "B",
                "describe": "Boundstone"
            }
        ]
    },
    {
        "label": "Br",
        "children": [
            {
                "value": 34,
                "label": "Br",
                "describe": "Breccia"
            }
        ]
    },
    {
        "label": "rubbled",
        "children": [
            {
                "value": 35,
                "label": "rubbled",
                "describe": ""
            }
        ]
    }
]

def getSubDir(val):
    for pl in LABELS:
        for l in pl['children']:
            if l['value'] == val:
                return pl['label'] + '/' + l['label'] + '/'
