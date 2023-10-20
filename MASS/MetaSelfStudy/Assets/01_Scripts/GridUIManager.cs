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
        
        int index = 0;

        for(int i = 0; i < height; i ++)
        {
            //열 생성
            GameObject column = Instantiate(columnF, gridTR);
            for(int j = 0; j < width; j ++)
            {
                //원소 생성
                GameObject element = Instantiate(elementF, column.transform);
                element.GetComponent<Element>().text.text = $"{index}";
                index++;
            }
        }
    }
}
