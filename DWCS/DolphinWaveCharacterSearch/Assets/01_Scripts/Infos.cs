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
        {0, "이루카"}
        ,{1, "미치루"}
        ,{4, "에렌"}
        ,{15, "비나"}
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
        kirisima, kazami, himuka, galatia
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
        handgun, sniperRifle, rocketLauncher, grenadeLauncher
    }


}


