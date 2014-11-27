from Tests.GenesisTests import GenesisTests
from Tests.FitnessTest import FitnessTest
from Tests.SelectionTest import SelectionTest
from Tests.RunnerTest import RunnerTest

def runGenesisTest():
	genesisTests = GenesisTests()
	genesisTests.run()

def runFitnessTest():
	fitnessTest = FitnessTest()
	fitnessTest.run()

def runSelectionTest():
	selectionTest = SelectionTest()
	selectionTest.run()
	selectionTest.checkDuplicates()

def runRunnerTest():
	runnerTest = RunnerTest()
	runnerTest.run()

#runGenesisTest()
#runFitnessTest()
#runSelectionTest()
runRunnerTest()