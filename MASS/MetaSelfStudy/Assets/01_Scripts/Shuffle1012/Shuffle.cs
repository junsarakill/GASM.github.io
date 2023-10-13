using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using UnityEngine;

public class Shuffle : MonoBehaviour
{
    //int 변수 100개를 담을 수 있는 배열
    public int[] intList;

    //담을 변수 개수
    [Range(1,100000)][SerializeField] int varAmount;
    
    void Update() {
        //1번으로 순차대로 숫자 넣기
        if(Input.GetKeyDown(KeyCode.Alpha1))
        {
            AddOrderIntList(out intList);
        }
        //2번으로 랜덤 int 넣기
        if(Input.GetKeyDown(KeyCode.Alpha2))
        {
            AddRandomInt2List(out intList);
        }

        if(Input.GetKeyDown(KeyCode.Alpha3))
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            intList = ListShuffle(intList);
            sw.Stop();
            UnityEngine.Debug.Log(sw.ElapsedMilliseconds+" ms");
        }
        if(Input.GetKeyDown(KeyCode.Alpha4))
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            intList = ShuffleRecur(intList);
            sw.Stop();
            print(sw.ElapsedMilliseconds+" ms");
        }

         if(Input.GetKeyDown(KeyCode.Alpha5))
         {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            ShuffleSwap(out intList);
            sw.Stop();
            UnityEngine.Debug.Log(sw.ElapsedMilliseconds+" ms");
        }
        
    }

    

    //배열 값을 인덱스로 채우기
    void AddOrderIntList(out int[] intList)
    {
        intList = new int[varAmount];
        for(int i = 0; i < intList.Length; i ++)
        {
            intList[i] = i;
        }
    }

    //지정된 개수만큼 배열에 랜덤 int 채우기
    void AddRandomInt2List(out int[] intList)
    {
        //배열 선언
        intList = new int[varAmount];
        //랜덤 int를 배열 원소에 넣기
        for(int i = 0; i < intList.Length; i ++)
        {
            intList[i] = Random.Range(0, 9999);
        }
    }

    //반복으로 셔플
    int[] ListShuffle(int[] list)
    {
        //배열 받아서 그 안의 원소의 순서를 랜덤으로 섞기
        /*
        셔플이란건 길이는 같은데 인덱스 순서를 다른게 하는것
        순차적으로 반복돌려서 랜덤 인덱스에 채우는 건 어떨까?
        <- 채워진 값에 중복으로 넣으면 안되는데 체크 해야함.
        순차대로 뽑아서 중복없는 가챠 박스를 만드는 느낌
        0~100 티켓이 하나씩 들어있는 가챠 박스
        뽑으면 없어짐

        */

        //배열을 리스트화
        List<int> tempList = list.ToList();
        //셔플되어 반환할 리스트
        List<int> shuffleList = new List<int>(tempList.Count);
        while(tempList.Count > 0)
        {
            //제거할 인덱스 랜덤으로 정하기
            int index = Random.Range(0, tempList.Count);
            //해당 값을 결과리스트에 추가하기
            shuffleList.Add(tempList[index]);
            //해당 값 제거하기
            tempList.RemoveAt(index);
        }
        
        //랜덤 리스트 반환하기
        return shuffleList.ToArray();
    }

    //재귀로 셔플하기
    int[] ShuffleRecur(int[] list, List<int> shuffledList = null)
    {

        if(shuffledList == null)
            shuffledList = new List<int>();
        //list가 없어질 때까지 반복해서 shuffledList에 넣기
        List<int> tempList = list.ToList();
        //제거할 인덱스 랜덤으로 정하기
        int index = Random.Range(0, tempList.Count);
        //해당 값을 결과리스트에 추가하기
        shuffledList.Add(tempList[index]);
        //해당 값 제거하기
        tempList.RemoveAt(index);

        //리스트에 원소가 남아있으면 다시 재귀
        if(tempList.Count > 0)
            return ShuffleRecur(tempList.ToArray(), shuffledList);
        //비었으면 셔플리스트 반환
        else
            return shuffledList.ToArray();

    }

    //@@ 멘토님 솔루션
    //교환 반복으로 셔플하기
    void ShuffleSwap(out int[] intList)
    {
        intList = this.intList;

        int n, m;

        for(int i = 0; i < intList.Length; i++)
        {
            n = Random.Range(0, intList.Length);
            m = Random.Range(0, intList.Length);

            var temp = intList[n];
            intList[n] = intList[m];
            intList[m] = temp;
        }
    }
}
