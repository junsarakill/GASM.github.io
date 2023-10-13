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
        ////2번으로 랜덤 int 넣기
        //if(Input.GetKeyDown(KeyCode.Alpha2))
        //{
        //    AddRandomInt2List(out intList);
        //}
        //랜덤 셔플 하기
        if(Input.GetKeyDown(KeyCode.Alpha3))
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            //intList = ListShuffle(intList);
            //intList = ShuffleRecur(intList);
            ShuffleSwap(out intList);
            sw.Stop();
            UnityEngine.Debug.Log(sw.ElapsedMilliseconds+" ms");
        }
        //오름차순 정렬하기
        if(Input.GetKeyDown(KeyCode.Alpha4))
        {
            //스톱워치 시작
            Stopwatch sw = new Stopwatch();
            sw.Start();
            //SelectSort(out intList);
            StartCoroutine(IESelectSort());
            //스톱워치 끝
            sw.Stop();
            print(sw.ElapsedMilliseconds+" ms 걸림");
        }
        
        
    }
#region 리스트 채우기
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

#endregion

#region 셔플
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

#endregion

#region 정렬
    //오름차순 정렬
    //선택정렬 : 현재 인덱스가 가장 작은 값이 될때까지 비교하기
    void SelectSort(out int[] intList)
    {
        intList = this.intList;

        for(int i = 0; i < intList.Length; i++)
        {
            //현재 인덱스 이후 원소를 전부 비교해서 스왑하기
            for(int j = i; j < intList.Length; j++)
            {
                if(intList[i] > intList[j])
                {
                    var temp = intList[i];
                    intList[i] = intList[j];
                    intList[j] = temp;
                }
            }
        }
    }
    //코루틴으로 천천히 변화 과정 보기
    //지연시간
    [SerializeField] float delayTime;
    IEnumerator IESelectSort()
    {
        WaitForSeconds ws = new WaitForSeconds(delayTime);
        for(int i = 0; i < intList.Length; i++)
        {
            //현재 인덱스 이후 원소를 전부 비교해서 스왑하기
            for(int j = i; j < intList.Length; j++)
            {
                if(intList[i] > intList[j])
                {
                    var temp = intList[i];
                    intList[i] = intList[j];
                    intList[j] = temp;
                }
                yield return ws;
            }
        }
        
    }
    
    //버블정렬 : 전부 정렬될때 까지 01,12,23,34 식으로 줄줄이 정렬하기

#endregion
}
