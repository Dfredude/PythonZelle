import json
class Attendee:
    def __init__(self, name:str, company:str, state:str, email:str) -> None:
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getAll(self):
        return self.getName, self.getCompany, self.getState, self.getEmail

    def getName(self):
        return self.name

    def getCompany(self):
        return self.company

    def getState(self):
        return self.state

    def getEmail(self):
        return self.email

class ConferenceAttendees:
    def __init__(self, infilename:str) -> None:
        self.infilename = infilename
        self.attendees = self.readDB(self.infilename)
        
    def readDB(self, infilename) -> dict:
        self.infilename = infilename
        infile = open(infilename, 'r')
        json_str = infile.read()
        attendees = json.loads(json_str)
        infile.close()
        return attendees
        
    def addAttendee(self, attendee):
        self.attendees['attendees'].append({       
                        "name": attendee.getName(),        
                        "company": attendee.getCompany(),
                        "state": attendee.getState(),
                        "email": attendee.getEmail()})

    def delAttendee(self, key:str, attribute:str):
        for i in range(len(self.attendees['attendees'])):
            if self.attendees['attendees'][i][key] == attribute:
                return self.attendees['attendees'].pop(i)

    def displayAttendee(self, key:str, attribute:str):
        for attendee in self.attendees['attendees']:
            if attendee[key] == attribute:
                return attendee

    def writeDB(self, outfilename):
        self.outfilename = outfilename
        outfile = open(self.outfilename, 'w')
        json_str = json.dumps(self.attendees)
        print(json_str, file= outfile)
        outfile.close()

if __name__ == '__main__':
    DataBase = ConferenceAttendees('Chapter-12/conferenceAttendees.json')
    MyAttendee = Attendee('Fred', 'Heben', 'B.C', 'd@gmail.com')
    DataBase.addAttendee(MyAttendee)
    print(DataBase.attendees['attendees'])
    DataBase.delAttendee('name', 'Chris')
    print(DataBase.attendees['attendees'])
    print(DataBase.displayAttendee('email', 'mjt@gmail.com'))
    DataBase.writeDB('Chapter-12/ConferenceAttendeesUpdated.json')
    
