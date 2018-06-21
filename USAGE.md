# API Room Scheduler

All awnswers of this API will be served on the JSON format.

## Rooms List: GET - /room
Return all created rooms. Each room has the following content:

| Attribute | Type | Description |
| --------- | -----| --------- |
| id | string | id of room, use it to retrieve the content of a given room |
| name | string | name of the room |
| capacity | int | the number of available seats of a given room |
| schedules | list | a list with the schedule of a given room |

**Example of usage:**

**Request** 
```
GET /room
```

**cURL** 
```
curl -X GET \
  http://localhost/room
```

**Reponse**
```
[
    {
        "_id": {
            "$oid": "5b292b83d2a3fa00b8290b51"
        },
        "name": "Coffee Room",
        "capacity": 3,
        "schedules": [
            {
                "title": "Planning",
                "participants": [
                    "Marcela",
                    "Barella"
                ],
                "begin": {
                    "$date": 1529074800000
                },
                "end": {
                    "$date": 1529082000000
                },
                "_id": {
                    "$oid": "5b292bfdd2a3fa00b8290b52"
                }
            }
        ]
    }
]
```

## Geting a given room: GET - /room/<room_id>
Return a schedule searched for it id.

**Example of usage:**

**Request** 
```
GET /room/5b292b83d2a3fa00b8290b51
```

**cURL** 
```
curl -X GET \
  http://localhost/room/5b292b83d2a3fa00b8290b51
```

**Reponse**
```
200 OK
```

## Create new room: POST - /room
Used to create a room

Currently, the allowed parameters are:

| Attribute | Type | Description |
| --------- | -----| --------- |
| name | string | set the desired name for the room |
| capacity | int | set the desired capacity for the room |

**Example of usage:**

**Request**
```
POST /room

{
    "name": "auditorium",
    "capacity": 30
}
```

**cURL**
```
curl -X POST \
  http://localhost/room \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "meeting room",
    "capacity": 10
}'
```

**Response**
```
201 CREATED
```

## Edit a Room: PUT - /room/<room_id>
Edit room details.
Currently, the allowed parameters are:

| Attribute | Type | Description |
| --------- | -----| --------- |
| name | string | set the name of the room for a new desired name |
| capacity | int | set the capacity of the room for a new desired capacity |

**Example of usage:**

**Request**
```
PUT /room/5b292b83d2a3fa00b8290b51

{
    "name": "auditorium",
    "capacity": 30
}
```

**cURL**
```
curl -X PUT \
  http://localhost:9080/room/5b292b83d2a3fa00b8290b51 \
  -d '{ \
    "name" : "auditorium", \
	"capacity": 30
}'
```

**Response**
```
204 NO CONTENT
```


## Delete a Room DELETE - /room/<room_id>
Used to delete a room

**Example of usage:**

**Request**
```
DELETE /room/5b29a326d2a3fa003f5992ba
```

**cURL**
```
curl -X DELETE \
  http://localhost/room/5b29a326d2a3fa003f5992ba
```

**Response**
```
200 OK
```

## List Schedules: GET - /room/<room_id>/schedule
Return all the schedules for a given room. Each schedule has the following content:

| Attribute | Type | Description |
| --------- | -----| --------- |
| id | string | id of a schedule, use it to retrieve the content of a given schedule |
| title | string | the title gived for the schedule to briefly explain the reason of it |
| participants | list | a list of strings with the name of the participants in a meeting |
| begin | string | the date of the beginning of a meeting. Example: "25-06-2018  |
| end | string | the date of the ending of a meeting. Example: "25-06-2018"  |

**Example of usage:**

**Request** 
```
GET /room/5b292b83d2a3fa00b8290b51/schedule
```

**cURL** 
```
curl -X GET \
  http://localhost/room/5b292b83d2a3fa00b8290b51/schedule
```

### Filtering Schedules:
You can also pass query parameters *begin_at_or_after* and/or *begin_at_or_before* to filter schedules. They are dates using *-* as separator. An example of date is: **24-06-1994**

Note:  
- begin_at_or_after will return all schedules that begin at or after given date
- begin_at_or_before will return all schedules that begin at or before given date
- you can use begin_at_or_after and begin_at_or_before together to retrieve a small set of schedules

**Examples of usage:**
**Request** 
```
GET /room/5b292b83d2a3fa00b8290b51/schedule?begin_at_or_after=24-06-1994
GET /room/5b292b83d2a3fa00b8290b51/schedule?end_at_or_before=24-06-1994
GET /room/5b292b83d2a3fa00b8290b51/schedule?begin_at_or_after=24-06-1994&end_at_or_before=30-06-1994
```

**cURL** d
```
curl -X GET http://localhost/room/5b292b83d2a3fa00b8290b51/schedule
curl -X GET http://localhost/room/5b292b83d2a3fa00b8290b51/schedule?end_at_or_before=24-06-1994
curl -X GET http://localhost/room/5b292b83d2a3fa00b8290b51/schedule?begin_at_or_after=24-06-1994&end_at_or_before=30-06-1994
```

**Reponse**
```
[
    {
        "title": "Planning",
        "participants": [
            "Marcela",
            "Barella"
        ],
        "begin": {
            "$date": 1529074800000
        },
        "end": {
            "$date": 1529082000000
        },
        "_id": {
            "$oid": "5b292bfdd2a3fa00b8290b52"
        }
    }
]
```

## Retrieve specific schedule: GET - /room/<room_id>/schedule/<schedule_id>
Retrieve a schedule searched by id.

**Example of usage:**

**Request** 
```
GET /room/5b292b83d2a3fa00b8290b51/schedule/5b292bfdd2a3fa00b8290b52
```

**cURL** 
```
curl -X GET \
  http://localhost/room/5b292b83d2a3fa00b8290b51/schedule/5b292bfdd2a3fa00b8290b52
```

**Reponse**
```
200 OK
```

## Edit a Schedule: PUT - /room/<room_id>/schedule/<schedule_id>
Used to make changes in a schedule

Currently, the allowed parameters are:

| Attribute | Type | Description |
| --------- | -----| --------- |
| title | string | set the title of the schedule for a new desired title |
| participants | list | change the participants in the participants meeting list  |
| begin | string | used to change the date and the time of a beginning of a meeting. If there's a meeting in the same date, time and room the operation will not be allowed |
| begin | string | used to change the date and the time of a ending of a meeting. If there's a meeting in the same date, and occuring in the same time in a given room, the operation will not be allowed |

**Example of usage:**

**Request**
```
PUT /room/5b292b83d2a3fa00b8290b51/schedule/5b292bfdd2a3fa00b8290b52

{
    "title": "coffee break",
    "articipants": ["Marcela", "Ricardo", "Camila"],
    "begin": "22/06/218 - 16:00",
    "end": "22/06/218 - 17:00",
}
```

**cURL**
```
```

**Response**
```
```

## Add a Schedule in a Room  POST - /room/<room_id>/schedule
Used to create a schedulein a given room.

Currently, the allowed parameters are:

| Attribute | Type | Description |
| --------- | -----| --------- |
| title | string | set the title for the schedule |
| participants | list | set the participants meeting list  |
| begin | string | used to set the date and the time of a beginning of a meeting. If there's a meeting in the same date, time and room the operation will not be allowed |
| begin | string | used to set the date and the time of a ending of a meeting. If there's a meeting in the same date, and occuring in the same time in a given room, the operation will not be allowed |

**Example of usage:**

**Request**
```
POST /room/5b292b83d2a3fa00b8290b51/schedule

{
    "title": "invetidors meeting",
    "articipants": ["Pamela", "Claudio", "Paulo", "Ana"],
    "begin": "27/08/2018 - 15:30",
    "end": "22/08/2018 - 17:45",
}
```

**cURL**
```
```

**Response**
```
201 CREATED
```

## Delete a Schedule of a Room DELETE - /room/<room_id>/schedule/<schedule_id>
Used to delete a schedule of a given.

**Example of usage:**

**Request**
```
DELETE /room/5b292b83d2a3fa00b8290b51/schedule/5b292bfdd2a3fa00b8290b52
```

**cURL**
```
```

**Response**
```
200 OK
```

## Searching for a Schedule date GET - /room/<room_id>/schedule/<schedule_id>

## Searching for a Schedule Room - GET - 







