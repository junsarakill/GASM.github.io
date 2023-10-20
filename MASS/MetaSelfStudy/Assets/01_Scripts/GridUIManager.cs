using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using System.Linq;

public class GridUIManager : MonoBehaviour
{
    //가로 세로 개수
    [Range(1,10)][SerializeField] int width,height;

    [SerializeField] float padding;

    //그리드
    [SerializeField]Transform gridTR;
    //시작 버튼
    [SerializeField]Button startBtn;

    //원소 프리팹
    [SerializeField]GameObject elementF;
    //column 프리팹
    [SerializeField]GameObject columnF;


    /*
    w = 3
    h = 2

    column 1 | e1,e2,e3
    column 2 | e1,e2,e3
    */

    private void Start() {
        startBtn.onClick.AddListener(MakeGraph);
    }

    private void Update() {
        if(Input.GetKeyDown(KeyCode.Space))
        {
            MakeGraph();
        }
    }

    //가로 세로 받아서 표 만들기
    void MakeGraph()
    {
        //표 비우기
        foreach(Transform child in gridTR)
        {
            Destroy(child.gameObject);
        }
        
        //원소 인덱스
        int index = 0;

        //RectTransform rt ;
        //rt.anchoredPosition = new Vector2(100, 100);


         
        //방법 1 이중 for

        //for(int i = 0; i < height; i ++)
        //{
        //    //열 생성
        //    GameObject column = Instantiate(columnF, gridTR);
        //    //위치 이동
        //    column.GetComponent<RectTransform>().Translate(0,i*(100 + padding),0);
        //    for(int j = 0; j < width; j ++)
        //    {
        //        //원소 생성
        //        GameObject element = Instantiate(elementF, column.transform);
        //        //위치 이동
        //        element.GetComponent<RectTransform>().Translate(j*(100 + padding),0,0);
        //        element.GetComponent<Element>().text.text = $"{index}";
        //        //인덱스 및 행 위치 증가
        //        index++;
        //    }
        //}

        //방법 2 while 이랑 dowhile
        while(index < width*height)
        {
            //나머지가 0일때 열 생성
            if(index % width == 0)
            {
                GameObject column = Instantiate(columnF, gridTR);
                //위치 이동
                column.GetComponent<RectTransform>().Translate(0,(index/width)*(100 + padding),0);

                //원소 하나 생성하고 다시 나머지가 0이 될때까지 원소 생성
                do
                {
                    GameObject element = Instantiate(elementF, column.transform);
                    //위치 이동
                    element.GetComponent<RectTransform>().Translate((index % width)*(100 + padding),0,0);
                    element.GetComponent<Element>().text.text = $"{index}";
                    index++;
                }
                while(index % width != 0);
            }
        }
    }

    void SetTRPosition()
    {

    }
}
