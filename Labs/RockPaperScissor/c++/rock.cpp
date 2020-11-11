#include <iostream>
#include <cstdlib>;
using namespace std;

int main()
{
	string weaponList[3] = {"Rock","Scissors","Paper"};
	int userWeapon;
	int computerWeapon;
	
	cout << "Please select 1. Rock, 2. Scissor, 3. Paper\n";
	cin >> userWeapon;
	userWeapon --;
	/* Get random integer less than 3*/
	computerWeapon = rand()%3;
	
	if (computerWeapon == userWeapon){
		cout << "A draw you both selected " << weaponList[computerWeapon] <<"\n";
	} else if ((userWeapon +1)%3 == computerWeapon){
		cout << "You win\n";
	} else if ((computerWeapon +1)%3 == userWeapon){
		cout << "Computer wins\n";
	}

	cout << weaponList[userWeapon] << " "<< weaponList[computerWeapon];

	return 0;
}