# Date: 01/14/2017
# Author: Krerkkiat Chusap
# Description:
# 	This Makefile will be used by the Git's hook script
# on the server. However, the hook script is not going to
# use the clean option. It will instead delete the whole
# repository directory.
# Also, the Git's hook is not going to be submitted since
# it does not seems to be part of the solution.
CXX=g++
LDFLAGS=
CXXFLAGS=-Wall -g

all: build

build:
	$(CXX) $(CXXFLAGS) $(LDFLAGS) main.cc

run:
	./a.out < ../examples/input1.dat
	./a.out < ../examples/input2.dat

clean:
	-rm -f a.out
