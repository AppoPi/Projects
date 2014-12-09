
#include "mynew.h"
#include "tcp.h"
#include <iostream>

using namespace std;

int TCP::isPrime(int n)
{
            if( n == 2 || n == 3 )
                return true;
            
            if( n == 1 || n % 2 == 0 )
                return false;
            
            for( int i = 3; i * i <= n; i += 2 )
                if( n % i == 0 )
                    return false;
            
            return true;
}

int TCP::nextPrime(int n)
{
        int i = n;
        while(!isPrime(i))
        {
                i++;
        }
        return i;
}

TCP::TCP(int numPort)
{
	hashSize = nextPrime(2*numPort);
 	hashTable = new HashEntry* [hashSize];
	for (int i = 0; i < hashSize; i++)
        	hashTable[i] = NULL;
//        int hash = 3  % hashSize;
//        hashTable[hash] = new HashEntry(3);
}  // TCP()

TCP::~TCP() {
}

void TCP::receive(int portNum, int packetNum, const char packet[257])
{
	int hash = portNum % hashSize;

	//while hash value is not empty && inserting value != present hash value
	//use linear probing to find empty hash value
	while (hashTable[hash] != NULL && hashTable[hash]->getPort() != portNum)
                hash = (hash + 1) % hashSize;
	if(maxDumped > packetNum);
	//if port is empty	
	if(hashTable[hash] == NULL)
	{
		hashTable[hash] = new HashEntry(portNum, new Node(packetNum, packet, NULL));
		
	}
	//if port is not empty, append packet to the end of list
	else if(hashTable[hash] != NULL && hashTable[hash]->getPort() == portNum)
	{
		listItr = hashTable[hash]->head;
		Node *temp = new Node(packetNum, packet, NULL);
		while(listItr->next != NULL)
		{
			listItr = listItr->next;
		}
		listItr->next = temp;
		hashTable[hash]->tail = listItr->next;
	}
        hashTable[hash]->upPackCount();
} // receive()

int TCP::getStream(int portNum, char stream[100000])
{

        int hash = portNum % hashSize;
        
        while (hashTable[hash] != NULL && hashTable[hash]->getPort() != portNum)
                hash = (hash + 1) % hashSize;
	
	hashTable[hash]->quickSort();
	hashTable[hash]->dumpStream(maxDumped, stream);

  // getStream() should fill the stream with current packets that have
  // packet numbers greater than the last packet past in the last 
  // stream for this port.  The packets must be ascending order, though
  // not necessarily consecutive.  Return the size of the stream in bytes.
  
   
   
   return 0;
}