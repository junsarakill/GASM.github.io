using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Food
{
    public int index = 0;
    public virtual void Eat()
    {
        Debug.Log("Food eat");
    }
}

public class Fruit : Food
{
    public override void Eat()
    {
        Debug.Log("Fruit Eat");
    }

    
}

public class Beverage : Food
{
    public new int index = 2;
    public override void Eat()
    {
        Debug.Log(GetType()+ " eat");
    }
}

public class ClassTest : MonoBehaviour
{
    Dictionary<object, object> aaa = new Dictionary<object, object>();

    // Start is called before the first frame update
    void Start()
    {
        //cTester();
        aaa.Add("asd", 22);
        aaa.Add(true, 344);
        aaa[123] = "bsa";
        
        string str = "";
        foreach(var key in aaa)
        {
            str += key + ", ";
        }
        print(str);
        print(aaa);
    }


    void cTester()
    {
        Food asd = new Food();
        asd.Eat();
        //Beverage ddd = new Beverage();
        //ddd.Eat();
        Food eee = new Beverage();
        //부모의 함수를 부르지만 자식의 함수가 사용됨
        eee.Eat();
        //0
        print(asd.index);
        // 역시 0 부모의 변수가 사용됨
        print(eee.index);
        // 캐스트 하고 나서야 자식의 변수 사용됨
        print(((Beverage) eee).index);
    }

    // Update is called once per frame
    void Update()
    {
    }
}
