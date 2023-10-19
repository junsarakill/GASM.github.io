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
    
    private void Start() {
        string a = "";
        Enumerable.Range(1,10).ToList().ForEach( (int i) => a += i);
        
    }
}
