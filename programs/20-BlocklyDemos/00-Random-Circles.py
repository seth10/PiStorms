#!/usr/bin/env python

# ATTENTION!
# Please do not manually edit the contents of this file
# Only use the web interface for editing
# Otherwise, the file may no longer be editable using the web interface, or you changes may be lost

# Copyright (c) 2016 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com

"""
--BLOCKLY FILE--
--START BLOCKS--
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9ImNvbnRyb2xzX3doaWxlVW50aWwiIGlkPSI4YixDUV8rIW4sd3pWYyE4IX5vbyIgeD0iNTEiIHk9IjYyIj48ZmllbGQgbmFtZT0iTU9ERSI+VU5USUw8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJCT09MIj48YmxvY2sgdHlwZT0ic3lzdGVtX2tleXByZXNzZWQiIGlkPSJtN3N5MS1kXm58ekR+cihzfmw2fCI+PC9ibG9jaz48L3ZhbHVlPjxzdGF0ZW1lbnQgbmFtZT0iRE8iPjxibG9jayB0eXBlPSJzY3JlZW5fZHJhd2NpcmNsZSIgaWQ9ImN7O1pudkQ/ZEd7XSooL3p7d2gyIj48ZmllbGQgbmFtZT0iQ09MT1IiPiNmZjAwMDA8L2ZpZWxkPjxmaWVsZCBuYW1lPSJESVNQTEFZIj5UUlVFPC9maWVsZD48dmFsdWUgbmFtZT0ieCI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9InApYFVwaDpNT25XOk9wLldENmJJIj48ZmllbGQgbmFtZT0iTlVNIj4xMDwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9Im5SWWJkSSteI2FCVzFudllTfHkwIiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iSCMqR1lJYGVrV2B3STtSZUssOyUiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IkozRkFKcTYhLV5WfjMxcHoyWG8zIj48ZmllbGQgbmFtZT0iTlVNIj4yMDA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iJSx4NUZqelJFKnU4OFpVSkc0UykiPjxmaWVsZCBuYW1lPSJOVU0iPjEwPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iYmpLLk8zbWNlVSVtNCNWZXdkQWUiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIjWnMwLktSKzkodntGVHo3dClSUiI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iSWwsXiFXST1SXyxIT2U1PWs4d1giPjxmaWVsZCBuYW1lPSJOVU0iPjIwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InJhZGl1cyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlZeUGxNSmpgVzUvNkMsXjFsck44Ij48ZmllbGQgbmFtZT0iTlVNIj4yNTwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9IldVeWZzV1U4QW0sUExCQ3dBakZXIiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iY1tYKThsPVNgbF4uMStsSFpsRDUiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9ImYzIypQZi1vZUNPdnB9Zy1oSUJbIj48ZmllbGQgbmFtZT0iTlVNIj43NTwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PG5leHQ+PGJsb2NrIHR5cGU9InNjcmVlbl9kcmF3Y2lyY2xlIiBpZD0iSTVfW2JURyUrIzdUazN8XlM5QygiPjxmaWVsZCBuYW1lPSJDT0xPUiI+I2ZmZmYwMDwvZmllbGQ+PGZpZWxkIG5hbWU9IkRJU1BMQVkiPlRSVUU8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJ4Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0icClgVXBoOk1Pblc6T3AuV0Q2YkkiPjxmaWVsZCBuYW1lPSJOVU0iPjEwPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iUGxUd18hYyVDUWk7RzlaRTJxPSUiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJXb1MpNENSVSFTIUItflNIYEQ4WyI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iak5ZLDg3LHwoVUNdfDs7UnNreFAiPjxmaWVsZCBuYW1lPSJOVU0iPjI1MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InkiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIlLHg1Rmp6UkUqdTg4WlVKRzRTKSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSJ5eHhQYk8lWytJQzVWZjFUbltiQSIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9InA3OSNiIXNvO3lKVHEwY2x0UGxAIj48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJIcSp6XVpqVDBsYTpHRjhgY3Q2MSI+PGZpZWxkIG5hbWU9Ik5VTSI+MjUwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iVl5QbE1KamBXNS82QyxeMWxyTjgiPjxmaWVsZCBuYW1lPSJOVU0iPjI1PC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0ibTFefEBtIyU6NUs/PUJrY0hrZkQiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJ3eT8yeW1PVSldYngtMT00bnkjZSI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iYFdBOmpVKjZGaG5fbm5GZVowUTUiPjxmaWVsZCBuYW1lPSJOVU0iPjEwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PG5leHQ+PGJsb2NrIHR5cGU9InNjcmVlbl9kcmF3Y2lyY2xlIiBpZD0iNkw1VyF9dDltIzFMQU0/LE18ITEiPjxmaWVsZCBuYW1lPSJDT0xPUiI+IzMzZmYzMzwvZmllbGQ+PGZpZWxkIG5hbWU9IkRJU1BMQVkiPlRSVUU8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJ4Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0icClgVXBoOk1Pblc6T3AuV0Q2YkkiPjxmaWVsZCBuYW1lPSJOVU0iPjEwPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iaXUxYVVEelcwSjIyIU95VT1COzciIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIvVFAzeUp3ZHFJV2dVfD9NXk9tXSI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0idnM2O0ovRUVxZCMsRTRaWlJiU30iPjxmaWVsZCBuYW1lPSJOVU0iPjMwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InkiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIlLHg1Rmp6UkUqdTg4WlVKRzRTKSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSJ6YC43SWdzXjB0cSs2VmtzbmpNYCIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9ImlXRG46R3YrRTdHYGdZeVBpKkNnIj48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJbdHw0KVt5R1JtRFRwaXxXaUFvZiI+PGZpZWxkIG5hbWU9Ik5VTSI+MzAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iVl5QbE1KamBXNS82QyxeMWxyTjgiPjxmaWVsZCBuYW1lPSJOVU0iPjI1PC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iUCFkN2ZtaS1OR3tqJVN1ZCNHJVoiIGlubGluZT0iZmFsc2UiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJnYjhhYk0rXk4lWXtUKmY4LkkhVCI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iNDBdKE1KXy4yZXZvNG53O0FnUlMiPjxmaWVsZCBuYW1lPSJOVU0iPjYwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJqO1BrdlpjMXMwKXJuOnMpPSNGeSIgaW5saW5lPSJ0cnVlIj48ZmllbGQgbmFtZT0iQ09MT1IiPiMzM2NjZmY8L2ZpZWxkPjxmaWVsZCBuYW1lPSJESVNQTEFZIj5UUlVFPC9maWVsZD48dmFsdWUgbmFtZT0ieCI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9InApYFVwaDpNT25XOk9wLldENmJJIj48ZmllbGQgbmFtZT0iTlVNIj4xMDwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9ImMuW3J0TUdpQnR8SlJBV0RAWCpaIiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iMChZP19oWlZORXNOeGs3NHBgWUYiPjxmaWVsZCBuYW1lPSJOVU0iPjgwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlYyeC5SSFtYNCtMRjlEKlYqVUZ3Ij48ZmllbGQgbmFtZT0iTlVNIj4zMDA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iJSx4NUZqelJFKnU4OFpVSkc0UykiPjxmaWVsZCBuYW1lPSJOVU0iPjEwPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iZF1qditQRV1DUlZ0SnZddCFKU04iIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJ2QTN8YlUhTDZrSnt0Y1RrbVFfKiI+PGZpZWxkIG5hbWU9Ik5VTSI+NzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iTFBYUyNqLTNCK3p1NEVRSHxwZjIiPjxmaWVsZCBuYW1lPSJOVU0iPjMwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InJhZGl1cyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlZeUGxNSmpgVzUvNkMsXjFsck44Ij48ZmllbGQgbmFtZT0iTlVNIj4yNTwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9IjRlNz0jX0AxX0ZSbSFCM1ZwO1RwIiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iUTdsMlgyekt0KEpnflF+YEZ4MXsiPjxmaWVsZCBuYW1lPSJOVU0iPjUwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Imlyb2cyaDtzYn07XSU5dDdifiVJIj48ZmllbGQgbmFtZT0iTlVNIj45MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwveG1sPg==
2d19063818498aba99a43c5a7ee9cab7babff1e957ce6a1746adf1a60c15e8be
--END BLOCKS--
"""


from PiStorms import PiStorms
import random

psm = PiStorms()


while not (bool(psm.isKeyPressed())):
  psm.screen.fillCircle((random.randint(30, 200)), (random.randint(30, 200)), (random.randint(30, 75)), (255, 0, 0), display = True)
  psm.screen.fillCircle((random.randint(30, 250)), (random.randint(30, 250)), (random.randint(30, 100)), (255, 255, 0), display = True)
  psm.screen.fillCircle((random.randint(30, 300)), (random.randint(30, 300)), (random.randint(30, 60)), (51, 255, 51), display = True)
  psm.screen.fillCircle((random.randint(80, 300)), (random.randint(70, 300)), (random.randint(50, 90)), (51, 204, 255), display = True)