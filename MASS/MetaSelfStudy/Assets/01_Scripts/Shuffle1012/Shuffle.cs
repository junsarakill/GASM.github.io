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

    //지연시간
    [SerializeField] float delayTime;
    WaitForSeconds delay;

    private void Awake() {
        delay = new WaitForSeconds(delayTime);
    }

    Coroutine bubblesortCor;
    
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
            SelectSort(out intList);
            //StartCoroutine(IESelectSort());
            //스톱워치 끝
            sw.Stop();
            print(sw.ElapsedMilliseconds+" ms 걸림");
        }
        if(Input.GetKeyDown(KeyCode.Alpha5))
        {
            //스톱워치 시작
            Stopwatch sw = new Stopwatch();
            sw.Start();
            //intList = BubbleSort(intList);
            intList = BubbleSort2(intList);
            //스톱워치 끝
            sw.Stop();
            print(sw.ElapsedMilliseconds+" ms 걸림");
        }
        if(Input.GetKeyDown(KeyCode.Alpha6))
        {
            //스톱워치 시작
            Stopwatch sw = new Stopwatch();
            sw.Start();
            intList = QuickSort(intList);
            //스톱워치 끝
            sw.Stop();
            print(sw.ElapsedMilliseconds+" ms 걸림");
        }
        if(Input.GetKeyDown(KeyCode.Alpha7))
        {
            //스톱워치 시작
            Stopwatch sw = new Stopwatch();
            sw.Start();
            System.Array.Sort(intList);
            //스톱워치 끝
            sw.Stop();
            print(sw.ElapsedMilliseconds+" ms 걸림");
        }

        if(Input.GetKeyDown(KeyCode.Alpha8))
        {
            StartCoroutine(IEQuickSort(intList, (c) =>
            {
                intList = c;
            }));
        }




        //if(Input.GetKeyDown(KeyCode.R))
        //{
        //    //스톱워치 시작
        //    Stopwatch sw = new Stopwatch();
        //    sw.Start();
        //    StartCoroutine(IEBubbleSort());
        //    StartCoroutine(IEStopwatchStop(sw));
        //}
        
        
    }
    public List<int> tempList;

    IEnumerator IEStopwatchStop(Stopwatch sw)
    {
        while(isCorRun)
        {
            yield return null;
        }
        //스톱워치 끝
        sw.Stop();
        print(sw.ElapsedMilliseconds+" ms 걸림");
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
    int[] SelectSort2(int[] intList)
    {
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

        return intList;
    }

    //코루틴으로 천천히 변화 과정 보기
    
    IEnumerator IESelectSort()
    {
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
                yield return delay;
            }
        }
        
    }
    
    //버블정렬 : 전부 정렬될때 까지 01,12,23,34 식으로 줄줄이 정렬하기
    //두개씩 묶어서 정렬 시키고 1번이라도 교환을 했는지 체크해서/교환 안하면 정렬 종료
    int[] BubbleSort(int[] intList)
    {
        bool isSwap = false;
        //0부터 length-2 까지 반복
        for(int i = 0; i < intList.Length-1; i++)
        {
            //자신,자신+1을 비교해서 작은 쪽을 왼쪽으로 스왑
            if(intList[i] > intList[i+1])
            {
                var temp = intList[i+1];
                intList[i+1] = intList[i];
                intList[i] = temp;
                //교환했음 체크
                if(!isSwap)
                    isSwap = true;
            }
        }
        
        //교환을 안했으면 리스트 반환
        //아니면 반복
        int[] returnList = isSwap ? BubbleSort(intList) : intList;

        return returnList;
    }

    int[] BubbleSort2(int[] intList)
    {
        bool isSwap;
        //한 번은 실행하도록 do while 사용
        do
        {
            isSwap = false;
            //0부터 length-2 까지 반복
            for(int i = 0; i < intList.Length-1; i++)
            {
                //자신,자신+1을 비교해서 작은 쪽을 왼쪽으로 스왑
                if(intList[i] > intList[i+1])
                {
                    var temp = intList[i+1];
                    intList[i+1] = intList[i];
                    intList[i] = temp;
                    //교환했음 체크
                    if(!isSwap)
                        isSwap = true;
                }
            }
        }
        while(isSwap);


        return intList;
    }

    IEnumerator IEBubbleSort()
    {
        isCorRun = true;
        bool isSwap = false;
        //0부터 length-2 까지 반복
        for(int i = 0; i < intList.Length-1; i++)
        {
            //자신,자신+1을 비교해서 작은 쪽을 왼쪽으로 스왑
            if(intList[i] > intList[i+1])
            {
                var temp = intList[i+1];
                intList[i+1] = intList[i];
                intList[i] = temp;
                //교환했음 체크
                if(!isSwap)
                    isSwap = true;
            }
            yield return delay;
        }
        
        //교환을 안했으면 리스트 반환
        //아니면 반복
        if(isSwap)
            StartCoroutine(IEBubbleSort());
        else
            isCorRun = false;
    }

    public bool isCorRun = false;

    //퀵 정렬
    /*불안정, 비교 정렬
    //리스트에 한 원소를 선택 = 이를 피벗이라함
    //피벗 기준 작은 원소는 왼쪽, 큰 건 오른쪽으로 옮기기
    피벗을 제외한 왼쪽,오른쪽 리스트를 다시 정렬
    재귀를 이용해 부분 리스트도 같은 방식을 사용
    부분 리스트가 분할이 불가능 = 크기가 0 or 1 까지 반복\
    */
    //정의에 부합하는 기본 퀵 정렬
    int[] QuickSort(int[] intAry)
    {
        //랜덤 인덱스 선택
        int index = UnityEngine.Random.Range(0, intAry.Length);
        List<int> leftList = new List<int>();
        List<int> rightList = new List<int>();
        for(int i = 0; i < intAry.Length; i++)
        {
        //인덱스는 스킵
            if(i == index)
                continue;
            
        //해당 원소를 기준으로 작은건 leftAry에 큰 건 rightAry로 놓기
            if(intAry[i] < intAry[index])
            {
                leftList.Add(intAry[i]);
            }
            else
            {
                rightList.Add(intAry[i]);
            }
        }
        //배열로 변환
        int[] leftAry = leftList.ToArray();
        int[] rightAry = rightList.ToArray();

        //크기가 2이상(정렬할 여지 있음) 이면 다시 퀵정렬 돌기
        if(leftList.Count > 1)
        {
            leftAry = QuickSort(leftAry);
        }
        
        if(rightList.Count > 1)
        {
            rightAry = QuickSort(rightAry);
        }

        //좌 배열 + 인덱스 + 우 배열 합치기
        int mergeLen = leftAry.Length + rightAry.Length + 1;

        int[] mergeAry = new int[mergeLen];
        
        leftAry.CopyTo(mergeAry, 0);
        mergeAry[leftAry.Length] = intAry[index];
        rightAry.CopyTo(mergeAry, leftAry.Length+1);

        return mergeAry;
    }

    //fixme
    IEnumerator IEQuickSort(int[] intAry, System.Action<int[]> callback)
    {
        print("시작");
        //랜덤 인덱스 선택
        int index = UnityEngine.Random.Range(0, intAry.Length);
        //좌우 리스트 선언
        List<int> leftList = new List<int>();
        List<int> rightList = new List<int>();
        for(int i = 0; i < intAry.Length; i ++)
        {
            //인덱스 스킵
            if(i == index)
                continue;
            
            //해당 인덱스의 원소 기준, 작은건 left, 큰 건 right로 놓기
            if(intAry[i] < intAry[index])
            {
                leftList.Add(intAry[i]);
            }
            else
            {
                rightList.Add(intAry[i]);
            }
            yield return null;
        }
        //배열로 변환
        int[] leftAry = leftList.ToArray();
        int[] rightAry = rightList.ToArray();
        

        //크기가 2이상 이면 다시 퀵정렬 돌기
        if(leftList.Count > 1)
        {
            StartCoroutine(IEQuickSort(leftAry, (c) =>
            {
                leftAry = c;
            }));
            while(leftAry != null)
                yield return null;
        }

        if(rightList.Count > 1)
        {
            StartCoroutine(IEQuickSort(rightAry, (c) =>
            {
                rightAry = c;
            }));
            while(rightAry != null)
                yield return null;
        }
        
        

        //좌 + 인덱스 + 우 배열 합치기
        int mergeLen = leftAry.Length + rightAry.Length + 1;
        int[] mergeAry = new int[mergeLen];

        leftAry.CopyTo(mergeAry, 0);
        mergeAry[leftAry.Length] = intAry[index];
        rightAry.CopyTo(mergeAry, leftAry.Length+1);

        callback(mergeAry);
    }
    
    int[] ConcatAry(int[] ary1, int num, int[] ary2)
    {
        int mergeLen = ary1.Length + ary2.Length + 1;
        int[] mergeAry = new int[mergeLen];

        ary1.CopyTo(mergeAry, 0);
        mergeAry[ary1.Length] = num;
        ary2.CopyTo(mergeAry, ary1.Length+1);

        return mergeAry;
    }
#endregion
}
