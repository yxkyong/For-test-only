# Tests.py

def test_een():
	# Test of een plus een twee is
	assert 1 + 1 == 2
	
def test_twee():
	# Test of een plus twee vijf is
	assert 1 + 2 == 5
	
def test_drie():
	# Test of je door 0 kan delen
	print 3/0
	
def test_vier():
	# Meerdere checks bij elkaar
	assert 1 + 1 == 2
	assert 2 + 2 == 4

# Je kan ook kijken of een test juist WEL een error gooit.
# Dit is handig als je wil testen of foute data juist behandeld wordt

from nose.tools import *

@raises(ZeroDivisionError) #
def test_vijf():
	# Deze test hoort een ZeroDivisionError te gooien
	0/0
