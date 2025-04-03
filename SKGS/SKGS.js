// cmn_cm 이미지 타입 : 256 아이콘 이미지

// 이미지 정보
/* 이미지 이름을 받아서 정보 파싱
   전문 예시: cmn_cm10000200
   8자리 숫자
   [0] : 레어도 : 1:n 2:r 3:sr 4:ssr 5:ur 6:lr
   [1] : 각성여부 : 0:통상 1:통상(특수) 2:각성 3: 신유제(변신)
   [2:4] : 캐릭터번호 : ex 000(아스카) 165(손권) 비어있는 번호 있음
   [5] : 속성 : 0:blue 1:red 2:yellow 3:purple 4:green
   [6:7] : 출시 순서 : 00~99 속성이 같을 시 출시 순에 따라 00,01,02 순으로 지어짐
 */
/* 프레임 이름 정보 파싱
    전문 예시 : cmn_cf_1000
    [0] : 레어도 이하략
    [1] : ?
    [2] : 속성 이하략
    [3] : 소속 : 0 : 선, 1 : 악, 2 : 무
*/
class imgInfo
{
    constructor(img_name = "cmn_cm87654321.png", img_url)
    {
        // 전문 6번째부터 끝까지가 id
        this.id = img_name.substring(6,14);
        // // 파일 전문
        // this.file_name = img_name;
        // url
        this.url = img_url;
        // id 0 번째 레어도
        this.rarity = this.id[0];
        // 각성 수준
        this.awake = this.id[1];
        // 캐릭터 번호
        this.name = this.id.substring(2,5);
        // 타입
        this.type = this.id[5];
        // 출시 순서
        this.release_order = this.id.substring(6,8);
        // 소속 : 선, 악, 무 : 전문으로 알 수 없는 하드 코딩 데이터
        this.division = this.getDiv();
        // 활성여부
        this.status = true;
    }

    /** 캐릭터 번호로 소속 결정
     * @param {string} this.name 캐릭터 번호
     * @returns {DIV} 소속
     */
    getDiv()
    {
        let result;
        // 캐릭터 번호 변환
        const CHAR_NUM = +this.name;
        // 선
        if(CHAR_NUM <= 4
        || (CHAR_NUM >= 10 && CHAR_NUM <= 14)
        || (CHAR_NUM >= 20 && CHAR_NUM <= 21)
        || CHAR_NUM == 25 || CHAR_NUM == 28
        || CHAR_NUM == 36 || (CHAR_NUM >= 100 && CHAR_NUM <= 102)
        || CHAR_NUM == 106 || (CHAR_NUM >= 111 && CHAR_NUM <= 113)
        )
        {
            result = DIV.SUN;
        }
        // 악
        else if((CHAR_NUM >= 5 && CHAR_NUM <= 9)
        || (CHAR_NUM >= 15 && CHAR_NUM <= 19)
        || CHAR_NUM == 26 || CHAR_NUM == 35 || CHAR_NUM == 37
        || CHAR_NUM == 49 || CHAR_NUM == 108 || CHAR_NUM == 124
        || (CHAR_NUM >= 140 && CHAR_NUM <= 144) || (CHAR_NUM >= 146 && CHAR_NUM <= 148)
        )
        {
            result = DIV.AK;
        }
        // 무
        else
            result = DIV.OTHER;

        return result;
    }
    
}

// 생성한 이미지 정보 객체를 담을 캐시 클래스
class imgInfoCache
{
    constructor()
    {
        // 이미지 캐시 불러오기
        const CACHED_DATA = localStorage.getItem("imgCache");
        // {id, imgInfo} 여러 개를 담은 캐시
        this.cache = CACHED_DATA ? JSON.parse(CACHED_DATA) : {};
    }

    /** 캐시에 있으면 주고 없으면 생성해서 주기
     * @param {string} img_name 이미지 전문
     * @param {string} img_url 이미지 주소
     * @returns {imgInfo} 이미지 정보 객체
     */
    getOrCreateImgInfo(img_name, img_url)
    {
        const ID = img_name.substring(6,14);

        // id 검색해서 있으면 반환
        if(this.cache[ID])
            return this.cache[ID];
        // 없으면 생성해서 저장 후 반환
        else
        {
            const NEW_IMG_INFO = new imgInfo(img_name, img_url);
            // 캐시에 저장
            this.cache[ID] = NEW_IMG_INFO;
            // 로컬 스토리지 업데이트

            return NEW_IMG_INFO;
        }        
    }

    /** data 배열 받아서 imgInfo 배열 반환
     * @param {string[]} img_data 이미지 전문, 이미지 주소 의 페어
     * @returns {imgInfo[]} 이미지 정보 배열
     */
    createImgInfos(img_data)
    {
        const IMG_INFOS = [];

        img_data.forEach(data => {
            // 더미 데이터 id 인지 확인
            if(!this.checkDummyData(data.name))
            {
                // 배열에 추가
                const IMG_INFO = this.getOrCreateImgInfo(data.name, data.url);
                IMG_INFOS.push(IMG_INFO);
            }
        });

        return IMG_INFOS;
    }

    // 캐시 데이터를 로컬 스토리지에 저장
    saveImgInfos()
    {
        localStorage.setItem("imgCache", JSON.stringify(this.cache));
    }

    // 더미 데이터 인지 확인
    checkDummyData(img_id)
    {
        // 확장자 빼기
        return DUMMY_ID_ARRAY.includes(img_id.substring(0,14));
    }
}

//#region 전역 변수

// 전체 이미지 이름 및 데이터 : 깃허브 api로 불러올 것
let all_img_data = null;
// 더미 데이터 정보 : 필요시 계속 추가해야함
const DUMMY_ID_ARRAY = [
    "cmn_cm52024003","cmn_cm40024003","cmn_cm51024003","cmn_cm10025000"
    ,"cmn_cm10026000","cmn_cm10028000","cmn_cm10035000","cmn_cm10036000"
    ,"cmn_cm10037000","cmn_cm20025100","cmn_cm20025200","cmn_cm20026100"
    ,"cmn_cm20026200","cmn_cm20028100","cmn_cm20028200","cmn_cm20035200"
    ,"cmn_cm20036100","cmn_cm20037100","cmn_cm20037200","cmn_cm30015200"
    ,"cmn_cm30025100","cmn_cm30025200","cmn_cm30026100","cmn_cm30026200"
    ,"cmn_cm30028100","cmn_cm30036200","cmn_cm40004000","cmn_cm40013401"
    ,"cmn_cm40024003","cmn_cm40028200","cmn_cm51024003","cmn_cm51030100"
    ,"cmn_cm51032000","cmn_cm51042100","cmn_cm52024003","cmn_cm51024103"
    ,"cmn_cm25025000","cmn_cm35025000","cmn_cm20026000","cmn_cm30026000"
    ,"cmn_cm20036000","cmn_cm30036000","cmn_cm30037000","cmn_cm10000100"
    ,"cmn_cm10002100","cmn_cm10003100","cmn_cm10005100","cmn_cm10006100"
    ,"cmn_cm10008100","cmn_cm10009100","cmn_cm10011100","cmn_cm10012100"
    ,"cmn_cm10014100","cmn_cm10015100","cmn_cm10017100","cmn_cm10018100"
    ,"cmn_cm10025100","cmn_cm10026100","cmn_cm10035100","cmn_cm10036100"
    ,"cmn_cm10037100","cmn_cm10001000","cmn_cm10000000","cmn_cm10003000"
    ,"cmn_cm10004000","cmn_cm10006000","cmn_cm10007000","cmn_cm10009000"
    ,"cmn_cm10010000","cmn_cm10012000","cmn_cm10013000","cmn_cm10015000"
    ,"cmn_cm10016000","cmn_cm10018000","cmn_cm10019000","cmn_cm10001200"
    ,"cmn_cm10002200","cmn_cm10004200","cmn_cm10005200","cmn_cm10007200"
    ,"cmn_cm10008200","cmn_cm10010200","cmn_cm10011200","cmn_cm10013200"
    ,"cmn_cm10014200","cmn_cm10016200","cmn_cm10017200","cmn_cm10019200"
    ,"cmn_cm10025200","cmn_cm10026200","cmn_cm10028200","cmn_cm10035200"
    ,"cmn_cm10036200","cmn_cm10037200","cmn_cm20025000","cmn_cm10028100"
];
// 특수 관계 맵 [이전 id : 다음 id] : 필요시 계속 추가해야함(신유제로 캐릭터가 바뀌는 경우등)
const SPECIAL_REL_IDS = new Map([
    ["40001100","52001100"] // 수영복 이카루가
    ,["52002301","53001302"] // 신유제 카츠라기 & 이카루가
    ,["30002200","42002202"] // 드림즈 카츠라기
    ,["62003001","62003001"] // 크리스마스 lr 야규
    ,["53003401","51004401"] // 기념 야규히바
    ,["30004201","52004251"] // 메이드 히바리
    ,["32005101","42005300"] // 호무라 원시 현속성
    ,["30005100","52005150"] // 호무라 d 엔젤
    ,["30007200","52007250"] // 온천 히카게
    ,["30008101","52008151"] // 무녀? 미라이
    ,["30008102","52008152"] // 마츠리 미라이
    ,["30008000","52008050"] // 드림즈 미라이
    ,["30009000","42009003"] // 헤비죠 하루카
    ,["30011000","52011050"] // 온천 무라쿠모
    ,["30012001","52012051"] // 차드 요자쿠라
    ,["62013203","62013203"] // 크리스마스 lr 시키
    ,["30014100","52014150"] // 바니걸 미노리
    ,["30014101","52014151"] // 서커스 미노리
    ,["30016200","52016250"] // 무녀? 무라사키
    ,["30017200","52017250"] // 제복? 이무
    ,["52019402","53018403"] // 신유제 료나 & 료비
    ,["30019100","52019150"] // 바니걸 료나
    ,["30028000","52028050"] // 마츠리 아야메
    ,["32028000","62028001"] // 목숨걸기 아야메
    ,["40034100","52034100"] // 요마둥지 카구라 1차
    ,["52034100","52034101"] // 요마둥지 카구라 2차
    ,["30037200","52037200"] // 인전신 소우지
    ,["30049100","52049100"] // 인전신 바쇼
    ,["40049100","52049102"] // 마츠리 바쇼
    ,["62108300","62108300"] // 크리스마스 lr 긴레이
    ,["51100004","51100005"] // 만우절 후부키
]);
// 이미지 정보 캐시
const IMG_CACHE = new imgInfoCache();
// 활성화된 필터 정보
let active_filters = {
    rarity : []
    ,type : []
};
// 깃허브 정보
const OWNER = "junsarakill";
const REPO = "GASM.github.io";
// google cloud function url
const GOOGLE_CLOUD_FUNCTION_URL = "https://us-central1-skgs-418602.cloudfunctions.net/SKGS_TEST";
// enum 소속
const DIV = { 
    SUN : 0,
    AK : 1,
    OTHER : 2
}
// 프레임 이미지 url
const FRAME_IMG_URL = `https://${OWNER}.github.io/${REPO}/SKGS/frame_img`;

// 이미지 관계 맵
const RELATION_MAP = new Map();
// 관계 유무 추적용
const USED_KEY = new Set();
const USED_VALUE = new Set();


//#endregion

//#region 시작 영역 main

// 웹페이지 로드 시
document.addEventListener("DOMContentLoaded", async () => {
    // 데이터 가져오기
    all_img_data = await getImgData();

    console.log("전체 데이터 : ", all_img_data);

    // 토글 버튼 클릭 이벤트 추가
    onClickFilterBtn();

    // 필터 설정 불러오기
    if(localStorage.getItem("active_filters"))
        active_filters = JSON.parse(localStorage.getItem("active_filters"));

    // 필터에 클릭 이벤트 추가
    document.querySelectorAll(".filter-btn").forEach(button => {
        // 필터 설정대로 활성화하기
        const IS_RARITY = button.dataset.rarity !== undefined;
        const CATEGORY = IS_RARITY ? "rarity" : "type";
        const VALUE = button.dataset.rarity || button.dataset.type;

        if(active_filters[CATEGORY].includes(VALUE))
            button.classList.add("active");

        // 필터 클릭 이벤트 추가
        button.addEventListener("click", function () {
            // 활성화 토글
            button.classList.toggle("active");

            // 필터 카테고리 설정
            const FILTER_CATEGORY = button.dataset.rarity !== undefined 
                ? "rarity" : "type";
            // 필터 카테고리 값 설정
            const FILTER_VALUE = button.dataset.rarity || button.dataset.type;

            updateFilter(FILTER_CATEGORY, FILTER_VALUE);
        });
    });

    //이미지 요소 생성
    main();
});

/** 이미지 데이터로 이미지 요소 생성
 */
function main()
{
    // 필터로 데이터 필터링
    let filtered_img_data = filterImg();

    console.log("필터링 된 데이터 : ", filtered_img_data);

    // 객체 생성
    let img_infos = IMG_CACHE.createImgInfos(filtered_img_data);
    // 이름과 속성 순 정렬
    // img_infos = sortImgInfo(img_infos);
    
    console.log("이미지 객체 : ", img_infos);

    // 관계도 맵 생성
    const REL_MAP = buildImgRelation(img_infos);

    console.log("관계도: ", REL_MAP);

    // 이미지 그루핑 및 정렬
    const IMG_GROUPS = sortImgGroup(imgGrouping(img_infos, REL_MAP));

    console.log("이미지 그룹 : ", IMG_GROUPS);

    // 그룹 가지고 이미지 생성
    generateImg(IMG_GROUPS);
}


//#endregion

//#region 필터 관련

/** 필터 정보 가져와서 필터링
 * @returns {string[][]} 필터링 된 이미지 데이터
 */
function filterImg()
{
    // 필터링 결과
    let filtered_img_data = all_img_data.filter(img_data => {
        const RARITY_MATCH = active_filters.rarity.length === 0 
        || active_filters.rarity.includes(img_data.rarity);
        const TYPE_MATCH = active_filters.type.length === 0 
        || active_filters.type.includes(img_data.type);

        return RARITY_MATCH && TYPE_MATCH;
    });

    // console.log(filtered_img_data);

    return filtered_img_data;
}

/** 필터 토글 버튼 클릭 이벤트 추가
 */
function onClickFilterBtn()
{
    let toggle_btn = document.getElementById("filter-toggle");
    let filter = document.getElementById("filter");

    toggle_btn.addEventListener("click", function () {
        if(filter.classList.contains("hide"))
        {
            filter.classList.remove("hide");
            toggle_btn.innerHTML = "&times;";
            toggle_btn.classList.add("toggle-right");
            // 토글 버튼 위치 이동
            let filter_width = filter.offsetWidth;
            toggle_btn.style.left = filter_width + "px";
        }
        else
        {
            filter.classList.add("hide");
            toggle_btn.innerHTML = "&#9776";
            toggle_btn.classList.remove("toggle-right");
            // 토글 버튼 위치 되돌리기
            toggle_btn.style.left = "0px";
        }
    });
}

/** 필터 클릭 이벤트 : 필터 업데이트
 * @param {string[]} category 레어도, 속성
 * @param {bool[]} value ON/OFF 유무
 */
function updateFilter(category, value)
{
    const INDEX = active_filters[category].indexOf(value);

    if(INDEX > -1)
        active_filters[category].splice(INDEX, 1);
    else
        active_filters[category].push(value);

    // 필터 값 로컬 스토리지에 저장
    localStorage.setItem("active_filters",JSON.stringify(active_filters));

    // 업데이트한 필터대로 이미지 요소 갱신
    main();
}

//#endregion

//#region 이미지 데이터 관련


/** 깃허브 api로 이미지 정보 가져오기
 * @returns {string[][]} 이미지 이름, 이미지 주소 페어
 */
function getImgData() {
    return fetch(GOOGLE_CLOUD_FUNCTION_URL, {
        method : "POST",
        headers : {
            "Content-Type" : "application/json",
        },
        body: JSON.stringify()
    })
    .then(response => {
        if(!response.ok)
            throw new Error("Network response was not ok");
        return response.json();
    })
    .then(data => {
        // console.log(data);

        return data;
    })
    .catch(error => {
        console.error(error);

        return [];
    });
}

//#endregion

//#region 이미지 객체 관련

/** 이미지 정보 객체 이름과 속성 순 정렬
 * @param {imgInfo[]} img_infos 이미지 객체 배열
 * @returns {imgInfo[]} 정렬된 배열
 */
function sortImgInfo(img_infos)
{
    img_infos.sort((a,b) => {
        if(a.name != b.name)
            return a.name.localeCompare(b.name);
        else
            return a.type.localeCompare(b.type);
    });

    return img_infos;
}

/** 이미지 그룹 정렬 : 이름 -> 레어도 -> 속성 오름차순
 * @param {imgInfo[][]} img_groups 이미지 그룹 여러 개를 가진 배열
 * @returns {imgInfo[][]} 정렬된 img_groups 반환
 */
function sortImgGroup(img_groups)
{
    img_groups.sort((img_group_a,img_group_b) => {
        const a = img_group_a[0];
        const b = img_group_b[0];
        // 이름 기준
        if(a.name != b.name)
            return a.name.localeCompare(b.name);
        // 레어도 기준
        else if(a.rarity != b.rarity)
            return a.rarity.localeCompare(b.rarity);
        //속성 기준
        else
            return a.type.localeCompare(b.type);
    });

    return img_groups;
}

/** 두 관련된 id를 관계 맵에 설정
 * @param {string} cur_id 이전 이미지 id
 * @param {string} next_id 다음 이미지 id
 */
function setRelMap(cur_id, next_id)
{
    // 관계 맵에 설정
    RELATION_MAP.set(cur_id, next_id);
    // 사용 횟수 추적 업데이트
    USED_KEY.add(next_id);
    USED_VALUE.add(cur_id);
}




/** 이미지 간 관계 설정
 * @param {imgInfo[]} img_infos 이미지 객체 배열
 * @returns {Map<imgInfo.id, imgInfo.id>} 이미지 관계 맵
 */
function buildImgRelation(img_infos)
{
    // 캐릭터 그룹 맵
    const CHAR_GROUP_MAP = new Map();

    // 캐릭터 그룹화
    img_infos.forEach(img_info => {
        // 특수 관계 설정
        if(SPECIAL_REL_IDS.has(img_info.id))
        {
            const NEXT_IMG_INFO = img_infos.find(e => e.id === SPECIAL_REL_IDS.get(img_info.id));

            if(NEXT_IMG_INFO)
                setRelMap(img_info.id, NEXT_IMG_INFO.id);
        }

        // 캐릭터 그룹이 없으면 추가하고 있으면 push
        if(!CHAR_GROUP_MAP.has(img_info.name))
            CHAR_GROUP_MAP.set(img_info.name, []);

        CHAR_GROUP_MAP.get(img_info.name).push(img_info);
    });

    // 그룹 내에서 원소를 비교
    CHAR_GROUP_MAP.forEach(char_group => {
        for(let i = char_group.length - 1; i >= 0; i--)
        {
            const CUR_ID = char_group[i].id;
            // key 로 사용되었는지 확인
            // 일반 이미지 검사 제외
            if(USED_KEY.has(CUR_ID) || char_group[i].awake === "0") 
                continue;

            // 우선도 1 : 레어도 차이
            let rarity_inc = 99;
            // 우선도 2 : 출시순서 비슷한 순
            let order_inc = 99;
            let id_cache;

            for(let j = char_group.length - 1; j >= 0; j--)
            {
                const OTHER_ID = char_group[j].id;
                // value로 사용되었는지 확인
                if(USED_VALUE.has(OTHER_ID) || j === i)
                    continue;
                // 관계성 확인
                else if(checkRelation(char_group[i], char_group[j]))
                {
                    // 우선도 확인
                    const NOW_RARITY_INC = Math.abs(parseInt(char_group[i].rarity - char_group[j].rarity));
                    const NOW_ORDER_INC = Math.abs(parseInt(char_group[i].release_order) - parseInt(char_group[j].release_order));

                    if(rarity_inc > NOW_RARITY_INC)
                    {
                        rarity_inc = NOW_RARITY_INC; 
                        order_inc = NOW_ORDER_INC;
                        id_cache = OTHER_ID;

                        // console.log(CUR_ID, OTHER_ID, id_cache);
                    }
                    else if(rarity_inc == NOW_RARITY_INC)
                    {
                        if(order_inc > NOW_ORDER_INC)
                        {
                            order_inc = NOW_ORDER_INC;
                            id_cache = OTHER_ID;
                        }
                    }
                }
            }

            // 관계 맵 추가
            if(id_cache)
                setRelMap(id_cache, CUR_ID);
        }
    });

    return RELATION_MAP;
}

/** 두 id 관계성 비교
 * @param {imgInfo} awake_img // 이미지 객체 1
 * @param {imgInfo} original_img // 이미지 객체 2
 * @returns {bool}
 */
function checkRelation(awake_img,original_img)
{
    //레어도, 각성 수준, 속성
    const RARITY1 = awake_img.rarity;
    const RARITY2 = original_img.rarity;
    const AWAKE1 = awake_img.awake;
    const AWAKE2 = original_img.awake;
    const TYPE1 = awake_img.type;
    const TYPE2 = original_img.type;

    // 캐릭터 번호가 같은지 확인
    if(awake_img.name !== original_img.name || TYPE1 !== TYPE2)
        return false;
    
    // 만약 신유제면 일반 각성인지 엄격하게 확인하기
    const IS_NOT_NEW_REL = AWAKE1 === "3" 
    && (AWAKE2 !== "2" || awake_img.release_order !== original_img.release_order
        || RARITY1 !== RARITY2 
        || TYPE1 !== TYPE2
        );

    // 레어도 변화가 있는지 확인
    if(AWAKE1 !== "3" && RARITY1 === RARITY2)
        return false;

    // 각성 변화 없는지 확인
    // 레어도, 각성 감소 확인
    // 레어도, 각성이 같은지 확인
    const IS_NOT_REL = ((AWAKE2 === "0" || AWAKE2 === "1") && AWAKE1 === AWAKE2)
    || RARITY1 < RARITY2
    || AWAKE1 < AWAKE2
    || (AWAKE1 === AWAKE2 && RARITY1 === RARITY2);

    // 모든 절차 통과
    return !IS_NOT_NEW_REL && !IS_NOT_REL;
}

/** 관계가 있는 이미지 객체 그룹 구하기
 * @param {imgInfo[]} img_infos 이미지 객체 배열
 * @param {Map<imgInfo.id, imgInfo.id>} rel_map 이미지 관계 맵
 * @returns {imgInfo[][]} 관계가 있는 이미지 객체 그룹
 */
function imgGrouping(img_infos, rel_map)
{
    // 인접 리스트 생성
    const ADJ_LIST = createAdjList(rel_map);

    // console.log("인접 리스트",ADJ_LIST);

    // 방문 기록
    const VISITED = [];
    // 이미지 그룹
    const IMG_GROUPS = [];
    // 모든 이미지 ID
    const ALL_ID = img_infos.reduce((ary, img_info) => {
        ary[img_info.id] = img_info;

        return ary;
    }, {});

    Object.keys(ALL_ID).forEach(img_id => {
        
        if(!VISITED[img_id]) {
            const GROUP = [];
            dfs(img_id, ADJ_LIST, VISITED, GROUP);
            IMG_GROUPS.push(GROUP.map(id => ALL_ID[id]));
        }
    });

    // img_infos.forEach(img_info => {
    //     // 미방문 id 일때
    //     if(!VISITED[img_info.id])
    //     {
    //         // 그룹 생성
    //         const GROUP = [];
    //         // dfs 로 그룹 찾기
    //         dfs(img_info.id, ADJ_LIST, VISITED, GROUP);
    //         IMG_GROUPS.push(GROUP.map(id => ALL_ID[id]));
    //     }
    // });

    return IMG_GROUPS;
}

/** 이미지 그루핑용 dfs
 * @param {imgInfo.id} img_id 이미지 id
 * @param {string[]} adj_list 인접리스트
 * @param {string[]} visited 방문 기록
 * @param {imgInfo.id[]} img_group 이미지 id 그룹
 */
function dfs(img_id, adj_list, visited, img_group)
{
    // 방문 true
    visited[img_id] = true;
    // 그룹에 추가
    img_group.push(img_id);
    
    // 인접 리스트에 id가 존재시
    if(adj_list[img_id])
    {
        // 인접 id에 전부 방문할 때까지 재귀
        adj_list[img_id].forEach(other_id => {
            if(!visited[other_id])
                dfs(other_id, adj_list, visited, img_group);
        });
    }
}

/** 인접 리스트 생성
 * @param {Map<imgInfo.id, imgInfo.id>} REL_MAP 이미지 관계 맵
 * @returns {string[]} 이미지 객체 관계 간선
 */
function createAdjList(REL_MAP)
{
    const ADJ_LIST = {};

    // 객체의 간선 관계 리스트로 정리
    REL_MAP.forEach((to, from) => {
        if(!ADJ_LIST[from])
            ADJ_LIST[from] = [];

        ADJ_LIST[from].push(to);
    });

    return ADJ_LIST;
}

//#endregion

//#region html 요소 관련

/**
 * 이미지 생성
 * @param {imgInfo[][]} IMG_GROUPS 이미지 그룹
 */
function generateImg(IMG_GROUPS)
{
    // 기존 list-content 요소 초기화
    // document.getElementById("list-content").innerHTML = '';
    let list_content = document.getElementById("list-content");
    
    while(list_content.firstChild)
    {
        list_content.removeChild(list_content.firstChild);
    }

    // 이중 for로 그룹 내 요소 하나하나 생성
    IMG_GROUPS.forEach(img_group => {
        // 그룹 컨테이너 생성
        const GROUP_CONTAINER = document.createElement("div");
        GROUP_CONTAINER.classList.add("img-group");
    
        // 이미지 생성 및 컨테이너에 추가
        img_group.forEach(img_info => {
            // 존재시 생성
            if(!img_info)
                return;

            // 이미지 컨테이너 생성
            const IMG_CONTAINER = document.createElement("div");
            IMG_CONTAINER.classList.add("img-container");

            // 이미지 요소 생성
            const IMG_ELEMENT = document.createElement("img");
            // 이미지 url 설정
            IMG_ELEMENT.src = img_info.url;
            IMG_ELEMENT.classList.add("raw-img");
            // 이미지 클릭 이벤트 추가
            IMG_CONTAINER.addEventListener("click", function() {
                // 상태 값 반전 
                img_info.status = !img_info.status;

                // 상태 값에 따라 비활성화 여부 결정
                imgToggleActive(IMG_CONTAINER, img_info.status);

                // 로컬 스토리지에 캐시 저장
                IMG_CACHE.saveImgInfos();
            });

            // 상태 값에 따라 비활성화 여부 결정
            imgToggleActive(IMG_CONTAINER, img_info.status);

            
            // 프레임 요소 생성
            const FRAME_ELEMENT = document.createElement("img");
            // 프레임 url 설정
            FRAME_ELEMENT.src = getImgFrame(img_info.rarity
                                            , img_info.type
                                            , img_info.division);
            FRAME_ELEMENT.classList.add("frame-img");


            // 툴팁 요소 생성
            const TOOLTIP = document.createElement("span");
            TOOLTIP.classList.add("tooltip");
            TOOLTIP.textContent = `id : ${img_info.id}`;

            // 컨테이너에 요소들 추가
            IMG_CONTAINER.appendChild(IMG_ELEMENT);
            IMG_CONTAINER.appendChild(FRAME_ELEMENT);
            IMG_CONTAINER.appendChild(TOOLTIP); 

            // 그룹 컨테이너에 추가
            GROUP_CONTAINER.appendChild(IMG_CONTAINER);
        });
        // list-content에 추가
        document.getElementById("list-content").appendChild(GROUP_CONTAINER);
    });
}

/** 활성화 여부에 따라 이미지 활성화
 * @param {IMG_ELEMENT} IMG_ELEMENT 이미지 요소
 * @param {bool} is_active 활성화 여부
 */
function imgToggleActive(IMG_ELEMENT, is_active)
{
    if(is_active)
        IMG_ELEMENT.classList.remove("deactive");
    else   
        IMG_ELEMENT.classList.add("deactive");
}

/** 프레임 이미지 url 조합
 * @param {string} rarity 레어도
 * @param {string} type 속성
 * @param {DIV} division 소속
 * @returns {string} 프레임 이미지 url
 */
function getImgFrame(rarity, type, division)
{
    // 결과 url string 조합
    const RESULT_URL = `${FRAME_IMG_URL}/cmn_cf_${rarity}0${type}${division}.png`;

    return RESULT_URL;
}

//#endregion
