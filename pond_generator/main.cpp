#include <iostream>
#include <fstream>

using namespace std;

main()
{
    ofstream file("pond.csv", ios::out);
    float pond[7];
    pond[0] = 1;
    pond[1] = 2;
    pond[2] = 3;
    pond[3] = 4;
    pond[4] = 5;
    pond[5] = 10;
    pond[6] = 20;

    for (int i=0; i<5; i++)
    {
        for (int j=0; j<5; j++)
        {
            for (int k=0; k<5; k++)
            {
                for (int l=0; l<5; l++)
                {
                    for (int m=0; m<3; m++)
                    {
                        for (int n=5; n<7; n++)
                        {
                            if(file)
                            {
                                file << pond[i] << ',' << pond[j] << ',' << pond[k] << ',' << pond[l] << ',' << pond[m] << ',' << pond[n] << endl;
                            }
                            else
                            {
                                cerr << "Erreur à l'ouverture !" << endl;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << endl;
    return 0;
}
