
class Key{
	int value;
	
	Key(int n){
		value = n;
	}
}

class Node{
	Key leftkey, rightkey;
	Node left, mid, right;
	
	public Node(){
		leftkey = null;
		rightkey = null;
	}
	
	public Node(int x){
		leftkey = new Key(x);
		rightkey = null;
	}
	
	public boolean isLeaf(){
		return leftkey == null && rightkey == null;
	}
	
	public int countKeys(){
		int keys = 0;
		if(leftkey != null) keys++;
		if(rightkey != null) keys++;
		return keys;
	}
}

public class TwoThreeTree{
	Node root;
	
	public boolean insert(int x){
		return insert(x, root, null);
	}
	
	public void printTree(){
		printTree(root);
	}
	
	/*
	 * Private helper functions
	 */
	
	private boolean insert(int x, Node subtree, Node parent){
		//Case 1: Tree is empty
		if(root == null){
			root = new Node(x);
			return true;
		}
		if(subtree.countKeys() == 0){
			subtree = new Node(x);
		}
		else if(subtree.countKeys() == 1){
			if (x < subtree.leftkey.value){
				subtree.rightkey.value = subtree.leftkey.value;
				subtree.leftkey = new Key(x);
			}
		} else if(subtree.countKeys() == 2){
			//Find parents connection
			char child = 'l';//LEFT
			if(parent.left == subtree) child = 'r';//RIGHT
			
			
			//Lower value than both keys
			if (x < subtree.leftkey.value){
				//Push up left key
				if(child == 'l'){
					
				}
					
			//Between both keys
			} else if (x > subtree.leftkey.value && x < subtree.rightkey.value){
				//Push Up Inserted key
			} else if (x > subtree.rightkey.value){
				//Push Up right key
			}
		}
		return false;
	}
	
	public void printTree(Node subtree){
		if(subtree.left != null){
			printTree(subtree.left);
		}
		if(subtree.leftkey != null){
			System.out.print(subtree.leftkey.value + ",");
		}
		if(subtree.mid != null){
			printTree(subtree.mid);
		}
		if(subtree.rightkey != null){
			System.out.print(subtree.rightkey.value + ",");
		}
		if(subtree.right != null){
			printTree(subtree.right);
		}
	}
	
	public static void main(String[] args){
		
		TwoThreeTree myTree = new TwoThreeTree();
		myTree.insert(5);
		myTree.insert(15);
		myTree.insert(13);
		myTree.insert(2);
		myTree.insert(3);
		myTree.insert(1);
		myTree.printTree();
	}
}



/*
if(x < subtree.leftkey.value){
	if(subtree.left != null){
		return insert(x, subtree.left);
	} else {
		subtree.left = new Node(x);
	}
} else if(x > subtree.leftkey.value){
	if(subtree.rightkey!=null){
		if(x < subtree.rightkey.value){
			if(subtree.mid != null){
				return insert(x, subtree.mid);
			} else {
				subtree.mid = new Node(x);
				return true;
			}
		} else if(x > subtree.rightkey.value){
			if(subtree.right != null){
				return insert(x, subtree.right);
			} else {
				subtree.right = new Node(x);
			}
		}
	} else {
		subtree.rightkey = new Key(x);
	}
}
*/
