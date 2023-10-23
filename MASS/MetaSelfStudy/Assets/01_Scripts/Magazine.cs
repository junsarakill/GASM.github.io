using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System.Linq;

public class MyStack
{
    
}

[System.Serializable]
//총알 클래스
public class Bullet
{
    public Bullet(string name, float damage, float pen)
    {
        this.name = name;
        this.damage = damage;
        this.pen = pen;
    }
    //이름
    public string name;
    //대미지
    public float damage;
    //관통력
    public float pen;
}

[System.Serializable]
//스택형 총알 뭉치 클래스(탄창, 탄약상자, 클립 등)
//@@ 리스트 말고 배열 + int 포인터로 재구성하기
public class BulletStack
{
    public BulletStack(string name = "", int maxAmount = 0)
    {
        this.name = name;
        this.maxAmount = maxAmount;
        curAmount = 0;
        bList = new List<Bullet>(maxAmount);
    }
    //이름
    public string name;
    //최대 용량
    public int maxAmount;
    //현재 용량
    public int curAmount;
    //한 발 차출
    public virtual Bullet Pop()
    {
        Bullet temp = bList[bList.Count-1];
        bList.Remove(temp);
        curAmount--;

        return temp;
    }
    //한 발 장전
    public virtual void Push(Bullet bullet)
    {
        bList.Add(bullet);
        curAmount = bList.Count;
    }

    //확인
    public virtual Bullet Peek()
    {
        return bList[bList.Count-1];
    }

    //리스트
    public List<Bullet> bList;

}

public class Magazine : MonoBehaviour
{
    //탄창 스택형
    
    [SerializeField] TextMeshProUGUI magTextUI;
    

    //한 발 차출

    //장전 
    [SerializeField]BulletStack mag = new BulletStack("tempMag", 30);

    private void Start() {
        Reload();
    }

    //30발 장전
    void Reload(int amount = 30)
    {
        for(int i = 0; i < amount; i++)
        {
            mag.Push(new Bullet($"{Random.Range(0,5)}",44,39));
        }
    }

    void Reload(Bullet bullet)
    {
        mag.Push(bullet);
    }
    
    private void Update() {
        if(Input.GetKeyDown(KeyCode.Alpha1))
        {
            Reload();
        }
        if(Input.GetKeyDown(KeyCode.Alpha2))
        {
            //한 발 차출
            print(mag.Pop().name);
        }
        if(Input.GetKeyDown(KeyCode.Alpha3))
        {
            //탄약 확인
            print(mag.Peek().name);
        }
        
    }
}
