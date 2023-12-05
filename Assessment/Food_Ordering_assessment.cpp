#include<iostream>
using namespace std;
class Food{
		public:
			int c,q,bill;
			string name,food,y,n;
			void menu()
			{
				cout<<"Please Enter Your Name: ";
				cin>>name;
				cout<<"Hello "<<name<<endl;
				cout<<"\nWhat would you like to order? "<<endl;
		     	cout<<"\n-------------Menu--------------"<<endl;

			    cout<<"\n1) Pizza";
			    cout<<"\n2) Burgers";
			    cout<<"\n3) Sandwich";
			    cout<<"\n4) Rolls";
			    cout<<"\n5) Biryani";
			    cout<<"\nPlease enter your choice: "<<endl;
			    cin>>c;
			    
			    if(c==1){
			    	cout<<"1) Cheese burst pizza Rs.230";
			    	cout<<"\n2) Farm fresh pizza Rs.250";
			    	cout<<"\n3) Panner pizza Rs.280";
			    	cout<<"\nPlease Enter which sandwhich you would like to have?:\n"; 
			    	cin>>c;
			    	if(c==1){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nCheese burst pizza";
						bill=q*230;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
			    	if(c==2){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nFarm fresh pizza";
						bill=q*250;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
			    	if(c==3){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nPanner pizza";
						bill=q*280;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
								
				}
				else if(c==2){
					cout<<"1)cheese Burger Rs.250";
					cout<<"\n2)Paneer Burger Rs.150";
					cout<<"\n3)Chicken Burger Rs.300";
					cout<<"\nPlease Enter which sandwhich you would like to have?:\n"; 
			    	cin>>c;
			    		if(c==1){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\ncheese Burger";
						bill=q*250;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
					
						if(c==2){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nPaneer Burger";
						bill=q*150;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
					
						if(c==3){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nChicken Burger";
						bill=q*300;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
					
				}
				else if(c==3){
					cout<<"1)Club Sandwich Rs.70";
					cout<<"\n2)Veg. Cripsy Sandwich Rs.80";
					cout<<"\n3)Extream Veg Sandwich Rs.120";
					cout<<"\nPlease Enter which sandwhich you would like to have?:\n"; 
			    	cin>>c;
			    	if(c==1){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nClub Sandwich";
						bill=q*70;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
				
			    	if(c==2){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nVeg. Cripsy Sandwich";
						bill=q*80;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
					
					if(c==3){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nExtream Veg Sandwich";
						bill=q*120;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
					}
				}
				
				
				else if(c==4){
					cout<<"1)Panner Rolls Rs.120";
					cout<<"\2)nchicken Rolls Rs.260";
					cout<<"\n3)Spring Roll Rs.120";
					cout<<"\nPlease Enter which sandwhich you would like to have?:\n"; 
			    	cin>>c;
			    	if(c==1){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nPanner Rolls";
						bill=q*120;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
			    	if(c==2){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nChicken Rolls";
						bill=q*260;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
			    	if(c==3){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nSpring Rolls";
						bill=q*120;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
				
				}
				else if(c==5){
					cout<<"1)Chicken Birayani Rs.180";
					cout<<"\n2)Veg. Birayani Rs.100";
					cout<<"\n3)Dum Birayani Rs.180";
					cout<<"\nPlease Enter which sandwhich you would like to have?:\n"; 
			    	cin>>c;
			    		if(c==1){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nChicken Birayani";
						bill=q*180;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
			    		if(c==2){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nVeg. Birayani";
						bill=q*100;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
			    		if(c==3){
			    		cout<<"\nPlease Enter Quantity: ";
						cin>>q;
						cout<<"\n-------------Your Order--------------"<<endl;
						cout<<"\nSDum Birayani";
						bill=q*180;
						cout<<"\nyour Total Bill is: "<<bill;
						cout<<"\nThank you for ordering Froms Tops Tech Fast Food";
				
				}
			    	
				}
				cout<<"\nWould you like to order anything else? y/n \n";
				cin>>y;
				if(y=="y"){
					menu();
				}
				else{
					cout<<"Thank you";
				}
				
			}		
	};

int main()
		{
		cout<<"\t\t\t\t\t\t\tTops Tech. Fast Food\n";
		Food f;
		f.menu();
		}

