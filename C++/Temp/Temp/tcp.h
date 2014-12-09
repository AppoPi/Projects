// Authors: Rin Tran, Alvin Chu
 
#ifndef TCP_H
#define	TCP_H

#include "mynew.h"
#include <cstring>
#include <iostream>
#define PACKET_SIZE 256

using namespace std;

class TCP 
{
public:
	struct Node
	{
		unsigned short packetNumber;
		char *packet;
		Node *next;
		Node(int pacNum, const char pac[257], Node *nex)
		{
			packetNumber = pacNum;
			packet = new char[257];
			strcpy(packet, pac);
			next = nex;
		}
		char *getPacket()
		{
			return packet;
		}
		unsigned short getPacketNumber()
		{
			return packetNumber;
		}
		
	
		~Node()
		{
			if(packet)
				delete[] packet;
		}
	};// packet node

	struct HashEntry
	{
	public:
		Node *head;
		Node *tail;
		unsigned short portNum;
		short maxPacketNum;
		short maxPacketDiscarded;
		short packetCount;
		HashEntry *next;

//		HashEntry(int pNum, HashEntry *nex)
		HashEntry(int pNum, Node* headNode)
		{
			head = headNode;
			tail = headNode;
			portNum = pNum;
			maxPacketNum = -1;
			maxPacketDiscarded = -1;
			packetCount = 0;
			//next = nex;
		}
		short getMaxDiscarded()
		{
			return maxPacketDiscarded;
		}
		void clearPort()
		{
    			Node *pDel = head;
    
    			/* Traverse the list and delete the node one by one from the head */
    			while (pDel != NULL)
    			{
        			/* take out the head node */
        			head = head->next;
       		 		delete pDel;
        			/* update the head node */
        			pDel = head;
    			}	
    			/* Reset the head and tail node */
    				tail = head = NULL;
		}





		
		void dumpStream(int maxdumped,char stream[100000])
		{
                        Node *Itr = head;
                        while(Itr)
                        {
                                strcat(stream, Itr->getPacket()); 
				if(maxdumped < Itr->getPacketNumber())
				{
					maxdumped = Itr->getPacketNumber();
				}
                                Itr = Itr->next;
                        }
			clearPort();
		}
		void quickSort()
		{
   		 	if (head != 0)
    			{
        			Node* current = head;
        			Node* prev = 0;
        			Node* tempNode = 0;
        			bool changeFlag = false;
        			for (int i = 0; i < packetCount; i++)
        			{
            				while (current->next != 0)
            				{
                				tempNode = current->next;

                				if (current->getPacketNumber() > tempNode->getPacketNumber())
                				{
                    					changeFlag = true;
                    					current->next = tempNode->next;
                    					tempNode->next = current;
                    					if (prev != 0)
                        				prev->next = tempNode;
                    					prev = tempNode;
                    					if (head == current)
                        				head = tempNode;
                    					if (current->next == 0)
                        				tail = current;
                				}
                				else
                				{
                    					prev = current;
                    					current = current->next;
                				}
            				}
            				if (changeFlag == false)
            		    			break;
            				else
            				{
                				prev = 0;
                				current = head;
                				changeFlag = false;
            				}
            			}		
            		}	
        	}
  

		

		void setMaxPacDiscarded(int packetNum)
		{
			if(maxPacketDiscarded < packetNum)
				maxPacketDiscarded = packetNum;
		}

		void upPackCount()
		{
			packetCount++;
		}	
		unsigned short getPort()
		{
        		return portNum;
		}
		void printMessage()
		{
			
			Node *Itr = head;
			while(Itr)
			{
				cout << Itr->getPacket() << endl;
				Itr = Itr->next;
			}
			cout << "Head: "<< head->getPacket() << endl;
			cout << "Tail: "<< tail->getPacket() << endl;
		}
	} **hashTable;
	int hashSize;
	int maxDumped;
	Node *listItr;
	int isPrime(int n);
	int nextPrime(int n);
	int hashFind(int portNum);
//	void sortPackets(Node* packets[], int packetCount);
			

  TCP(int numPorts);
  virtual ~TCP();
  void receive(int portNum, int packetNum, const char packet[257]);
  int getStream(int portNum, char stream[100000]);
};

#endif	/* TCP_H */
