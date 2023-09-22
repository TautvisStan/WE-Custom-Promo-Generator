class basePromoData:
    def __init__(self, titleEntry, descEntry, wrestlersEntry, team1Var, team2Var, refVar, useNamesVar, surpirseEntrantsEntry, nextPromoEntry):
        self.titleEntry = titleEntry
        self.descEntry = descEntry
        self.wrestlersEntry = wrestlersEntry
        self.team1Var = team1Var
        self.team2Var = team2Var
        self.refVar = refVar
        self.fileDirectory = '.'
        self.useNamesVar = useNamesVar
        self.surpriseEntrantsEntry = surpirseEntrantsEntry
        self.nextPromoEntry = nextPromoEntry
    
class singlePageData:
    def __init__(self, line1Entry, line2Entry, speakerEntry, receiverEntry, tauntEntry, demeanorEntry, featureData):
        self.line1Entry = line1Entry
        self.line2Entry = line2Entry
        self.speakerEntry = speakerEntry
        self.receiverEntry = receiverEntry
        self.tauntEntry = tauntEntry
        self.demeanorEntry = demeanorEntry
        self.featureData = []
        self.featurePos = 0;
        
class singleFeatureData:
    def __init__(self, featureEntry):
        self.featureEntry = featureEntry