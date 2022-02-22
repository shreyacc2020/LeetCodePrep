

int getSum(long long int a, long long int b){
    unsigned int c = 1;
    while (b!=0){
        long long int temp = (unsigned)(a&b)<< c;
        a = a^b;
        b = temp;
    }
    return a;
}