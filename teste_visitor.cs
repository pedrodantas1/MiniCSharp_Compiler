public class Teste1{
    private string s = new string("olá");

    Teste1(){
    }

    private static int func(){
        const int a = 43, b=32,c=11;
        int a=12,b=22,c=2;
        func2(a,b,c);
        func();
        string a = new string("ola mundo!");
        string b = new string();
        switch (a){
            case < 30:
                b = 50;
                break;
            case 50:
                b = 20;
                break;
            case null:
                b = 100;
                break;
            default:
                b = 0;
                break;
        }
        while(cliente == true){
            i++;
        }
        do{
            a = a*2;
        }while(a<250 && b > 45);
        int cont = 0;
        foreach(char c in "palavra"){
            cont++;
            continue;
        }
        double d = 3.2;
        int n = (int) d;
        int y = x << 4;
        return (a != 3) ? 1 : 22;
    }
}

class Teste2 {
    
}

class Teste3 {
    private static int x = 2;
    const int y = 33;
    private float altura;

    public Teste3(float altura){
        this.altura = altura;
    }

    public void func1(){
        bool cliente = false;
        int i=0;
        while(cliente == true)
        {
            i++;
        }
        double valor = 2 * (8 - 4 + (3 - 1));
        int a = -77+1;
        --a = a++;
        int b,c,d;
    }

    static int func2(int a, float y, string z){
        bool existe = false;
        if (a == 1){
            if (y != 20){
                return a;
            }
        }else{
            return 12;
        }
    }

    void func3(){
        int a = 1;
        for(int i=0; i<10; i++){
            a = a * 2;
        }
    }
    void func4(int z, float x){
        return;
    }
}