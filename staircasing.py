

class staircaseFunction():

    def __init__(self, maxNTrials, maxNReversals, startGuess, nUp, nDown):
        self.response = [0] * maxNTrials   #trial by trial record of observer correct/incorrect responses
        self.level = [0] * maxNTrials      # trial by trial record of match level
        self.condFinished = 0                # record of when condition finished (either max # trials or desired # staircase reversals
        self.stepSize = 0.200              # staircase starts with large stepsize, then is halved after 1 and 3 reversals
        self.stepSizeMin = 0.033
        self.nReversals = 0                  # record of # staircase reversals
        self.nReversalsSinceReset = 0                  # record of # staircase reversals
        self.trialsSinceReversal = 1
        self.revLevel = [0] * maxNTrials  # record of match level at reversal, used to calculate mean at end of run
        self.level[0] = startGuess  # 1st matching level is set by experimenter +/- 0 to 2 steps
        self.nPresented = 0                   # count how many trials have been matched for each condition
        self.nUp = nUp                     # count how many trials incorrect before raising staircase.
        self.nDown = nDown                         # count how many trials correct before lowering staircase.
        self.nYes = 0                     # count how many trials Yes
        self.nNo = 0                         # count how many trials No
        self.lastSign = 0                     # memory of level change
        self.selfSign = 0                     # new level change
        self.testLevel = self.level[self.nPresented]
        self.maxNTrials = maxNTrials
        self.maxNTReversals = maxNReversals
        self.stairBounds = [0.033, 1]

    def update(self, response):
        if not (response == 1 or response == 0):
            ValueError("Incorrect accuracy input, staircase is not updated. Accuracy should be either 1 or 0 in integer type. ")
            return None
        elif self.nPresented + 1 == self.maxNTrials:
            InterruptedError("Completed all staircase trials, update procedure is interrupted.")
            return None
            
        if (response == 1):  # correct or 'Yes' response
            self.response[self.nPresented] = 1
            self.nYes = self.nYes+1    # increment yes count
            self.nNo = 0                # zero no count
        else:# incorrect or No response
            self.response[self.nPresented] = 0
            self.nNo = self.nNo+1      # increment no count
            self.nYes = 0               # zero yes count
    
        if (self.nPresented == self.maxNTrials or self.nReversals == self.maxNTReversals): # if enough trials or reversals reached, terminate condition
            self.condFinished = 1       

        
        self.lastSign = self.selfSign
        self.nPresented = self.nPresented+1 # increment # trials
        self.trialsSinceReversal = self.trialsSinceReversal+1

        if (self.nYes == self.nDown): # target # Yes's in a row - lower staircase
            if (self.level[self.nPresented-1] - self.stepSize) >= self.stairBounds[0]:
                self.level[self.nPresented] = self.level[self.nPresented-1] - self.stepSize # reduce test level
            else: 
                self.level[self.nPresented] = self.stairBounds[0]
            self.selfSign = -1 # self staircase going down
            self.nYes = 0 # reset # Yes's in a row

        elif (self.nNo == self.nUp): # target # No's in a row - increase staircase
            if (self.level[self.nPresented-1] + self.stepSize) <= self.stairBounds[1]:
                self.level[self.nPresented] = self.level[self.nPresented-1] + self.stepSize # increase test level
            else: 
                self.level[self.nPresented] = self.stairBounds[1]            
            
            self.selfSign = 1 # self staircase going up
            self.nNo = 0 # reset # No's in a row

        else: # no change
            self.level[self.nPresented] = self.level[self.nPresented-1] 
            self.selfSign = self.lastSign # self staircase stays in same direction
        
        if (self.selfSign * self.lastSign == -1): # staircase changed direction
            self.nReversals = self.nReversals+1 # increment v c vb# reversals
            self.nReversalsSinceReset = self.nReversalsSinceReset+1
            self.trialsSinceReversal = 1#number of trials since last reversal
            self.revLevel[self.nReversals-1] = self.level[self.nPresented] # record level at which observer's response changed
            if self.stepSize * 0.80 >= self.stepSizeMin:
                self.stepSize = self.stepSize * 0.80
            else: 
                self.stepSize = self.stepSizeMin
        self.testLevel = self.level[self.nPresented]

      
textDurPractice = 0.5 #text duration (in seconds) for practice
trialsPerStaircase = 80 # trials per staircase
staircaseStart = 0.3 #staircase start point (300 ms)
staircasesPerFont = 1 # #number of staircases per font


