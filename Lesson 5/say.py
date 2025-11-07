import cowsay
import sys

#using the install librarie "cowsay"
if len(sys.argv) == 2:
  cowsay.cow("Hello, " + sys.argv[1])

if len(sys.argv) == 2:
  cowsay.trex("Hello, " + sys.argv[1])