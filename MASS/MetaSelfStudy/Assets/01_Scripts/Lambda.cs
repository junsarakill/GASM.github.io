using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class Lambda : MonoBehaviour
{
    public List<int> linqTest = new List<int>{
        1,23,656,2344,13,6553,123213,22,1,6,8,567
    };


    private void Start() {
        //Enumerable.Range(0,10).ToList().ForEach((int i ) => print(i));

        var oddSort = 
            from num in linqTest
            where(num % 2) != 0
            orderby num descending
            select num;

        print(oddSort.ToList());



        string printer = "[";
        oddSort.ToList().ForEach((int i ) =>{
            printer += printer == "[" ? i : $", {i}";
        });
        printer += "]";
        print(printer);

        string printer2 = "[";
        linqTest.ToList().ForEach((int i ) =>{
            printer2 += printer2 == "[" ? i : $", {i}";
        });
        printer2 += "]";
        print(printer2);
    }
}
