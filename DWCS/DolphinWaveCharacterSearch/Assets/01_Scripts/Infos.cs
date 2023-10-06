using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//전체 돌핀 데이터
public struct AllDolphineInfo
{
    List<DolphinInfo> jsonData;
}

//돌핀 정보
[System.Serializable]
public struct DolphinInfo
{
    //캐릭터 아이디
    public int id;
    //이름
    public string name;
    //옷 이름
    public string clothName;
    //레어도
    public StaticInfo.rarity rarity;
    //속성
    public StaticInfo.type type;
    //포지션
    public StaticInfo.Position position;
    //역할
    public StaticInfo.Role role;
    //소속
    public StaticInfo.team team;
    //스킬1 정보
    public SkillInfo skill1;
    //스킬2 정보
    public SkillInfo skill2;
    //sp 스킬 정보
    public SkillInfo skillSP;
}

//스킬 정보
[System.Serializable]
public struct SkillInfo
{
    //@@ 스킬 내용
    public string content;
    //무기 타입
    public StaticInfo.Weapon type;
}

//정해진 정보
[System.Serializable]
public static class StaticInfo
{
    //캐릭터 아이디 : 이름
    public static Dictionary<int, string> nameDict = new Dictionary<int, string>()
    {
        {0, "이루카"},
        {1, "미치루"},
        {2, "키리3"},
        {3, "안리"},
        {4, "에렌"},
        {5, "히요리"},
        {6, "카자3"},
        {7, "카자4"},
        {8, "히무카1"},
        {9, "히무카2"},
        {10, "히무카3"},
        {11, "히무카4"},
        {12, "우라미1"},
        {13, "우라미2"},
        {14, "우라미3"},
        {15, "우라미4"},
        {16, "세레나"},
        {17, "시온"},
        {18, "갤러3"},
        {19, "비나"},
        {20, "해설1"},
        {21, "해설2"},
        {21, "해설3"},
        {21, "해설4"},
        {22, "ai1"},
        {23, "ai2"},
        {24, "ai3"},
        {25, "ai4"}
    };
    //레어도
    public enum rarity
    {
        n, sr, ssr, ur
    }
    //포지션
    public enum Position
    {
        Attack, Defender
    }
    //역할
    public enum Role
    {
        Gunner, Rider
    }
    //속성
    public enum type
    {
        wave, sun, gear, moon, wind
    }
    //소속
    public enum team
    {
        kirisima, kazami, himuka, urami, galatia, maruTV
    }
    //소속 계산
    public static team GetTeam(int id)
    {
        //캐릭터 아이디 : 소속 = id % 4
        return (team)(id % 4);
    }
    //무기 종류
    public enum Weapon
    {
        handgun, sniperRifle, rocketLauncher, grenadeLauncher, shotgun
    }


}


