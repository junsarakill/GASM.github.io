using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class InputDolphin : MonoBehaviour
{
    //ui 구조 가지고 있기
    //id
    [SerializeField] TMP_InputField idIF;
    //clothName
    [SerializeField] TMP_InputField clothNameIF;
    //rare
    [SerializeField] GameObject rarity;
    //type
    [SerializeField] GameObject type;
    //pos
    [SerializeField] GameObject pos;
    //role
    [SerializeField] GameObject role;
    //skill1,2,sp
    [SerializeField] GameObject skill;
    //add
    [SerializeField] Button addBtn;

    private void Awake() {
        //버튼들 가져오기
        Button[] rarityBtns = rarity.GetComponentsInChildren<Button>();
        Button[] typeBtns = type.GetComponentsInChildren<Button>();
        Button[] posBtns = pos.GetComponentsInChildren<Button>();
        Button[] roleBtns = role.GetComponentsInChildren<Button>();
        Button[] skillBtns = skill.GetComponentsInChildren<Button>();
        
    }

    private void Start() {
    }
}
