from Tests.GenesisTests import GenesisTests
from Tests.FitnessTest import FitnessTest
from Tests.SelectionTest import SelectionTest

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

runGenesisTest()
runFitnessTest()
runSelectionTest()