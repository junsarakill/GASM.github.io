// 이미지 번호 분석하기
// 캐릭터별 폴더 생성 후 이미지 이동
// cmn_mn 이미지 타입 : 256 아이콘 이미지

// 캐릭터 번호 맵 만들려 했는데 굳이 필요 없나?

// 이미지 정보
/* 이미지 이름을 받아서 정보 파싱
   전문 예시: cmn_cx10000200
   8자리 숫자
   [0] : 레어도 - 1:n 2:r 3:sr 4:ssr 5:ur 6:lr
   [1] : 각성여부 - 0:통상 1:통상(특수) 2:각성 3: 신유제(변신)
   [2:4] : 캐릭터번호 - ex 000(아스카) 165(손권) 비어있는 번호 있음
   [5] : 속성 - 0:blue 1:red 2:yellow 3:purple 4:green
   [6:7] : 출시 순서 - 00~99 속성이 같을 시 출시 순에 따라 00,01,02 순으로 지어짐
 */
class imgInfo
{
    constructor(img_name = "cmn_cx87654321.png", img_url)
    {
        // 전문 6번째부터 끝까지가 id
        this.id = img_name.substring(6,14);
        // 파일 전문
        this.file_name = img_name;
        // url
        this.url = img_url;
        // id 0 번째 레어도
        this.rarity = this.id[0];
        // 이름 번호
        this.name = this.id.substring(2,5);
        // 타입
        this.type = this.id[5];
        // 활성여부
        this.status = true;
    }
}

// 생성한 이미지 정보 객체를 담을 캐시 클래스
class imgInfoCache
{
    constructor()
    {
        this.cache = {};
    }

    // 캐시에 있으면 주고 없으면 생성해서 주기
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

            return NEW_IMG_INFO;
        }        
    }

    // data 배열 받아서 imgInfo 배열 반환
    createImgInfos(img_data)
    {
        const IMG_INFOS = [];

        img_data.forEach(data => {
            const IMG_INFO = this.getOrCreateImgInfo(data.name, data.url);
            IMG_INFOS.push(IMG_INFO);
        });

        return IMG_INFOS;
    }
}

// 전체 이미지 이름 및 데이터
let all_img_data = null;
// 이미지 정보 캐시
const IMG_CACHE = new imgInfoCache();
// 활성화된 필터 정보
let active_filters = {
    rarity : []
    ,type : []
};

// 필터 업데이트
function updateFilter(category, value)
{
    const index = active_filters[category].indexOf(value);

    if(index > -1)
        active_filters[category].splice(index, 1);
    else
        active_filters[category].push(value);

    // 업데이트한 필터대로 필터링
    filterImg();
}

// 사실상 main
// 웹페이지 로드 시
document.addEventListener("DOMContentLoaded", async (event) => {
    // 데이터 가져오기
    all_img_data = await getImgData();
    console.log("전체 데이터 : ", all_img_data);

    // 토글 버튼 클릭 이벤트 추가
    onClickFilterBtn();
    // 필터에 클릭 이벤트 추가
    document.querySelectorAll(".filter-btn").forEach(button => {
        button.addEventListener("click", function () {
            // 활성화 토글
            button.classList.toggle("active");

            const filterCategory = button.dataset.rarity !== undefined ? "rarity" : "type";
            const filterValue = button.dataset.rarity || button.dataset.type;

            updateFilter(filterCategory, filterValue);
        });
    });

    // 필터 정보 가져와서 요소 생성
    filterImg();
});

// 토글 버튼 클릭 이벤트 추가
function onClickFilterBtn()
{
    var toggleBtn = document.getElementById("toggle_filter");
    var filter = document.getElementById("filter");

    toggleBtn.addEventListener("click", function () {
        if(filter.classList.contains("hide"))
        {
            filter.classList.remove("hide");
            toggleBtn.innerHTML = "&times;";
        }
        else
        {
            filter.classList.add("hide");
            toggleBtn.innerHTML = "&#9776";
        }
    });
}

// 이미지 객체 생성
function createImgElement(img_data)
{
    
    // 객체 생성
    // let img_infos = createImgInfo(img_data);
    let img_infos = IMG_CACHE.createImgInfos(img_data);

    // console.log(img_infos);

    // 이름과 속성 순 정렬
    img_infos = sortImgInfo(img_infos);

    // 관계도 맵 생성
    const REL_MAP = buildImgRelation(img_infos);

    // console.log(REL_MAP);

    // 이미지 그루핑
    const IMG_GROUPS = imgGrouping(img_infos, REL_MAP);

    console.log("이미지 그룹 : ", IMG_GROUPS);

    // 그룹 가지고 이미지 생성
    generateImg(IMG_GROUPS);
}

// 필터 정보 가져와서 필터링
function filterImg()
{
    // 필터링 결과
    let filtered_img_data = all_img_data.filter(img_data => {
        const rarity_match = active_filters.rarity.length === 0 
        || active_filters.rarity.includes(img_data.rarity);
        const type_match = active_filters.type.length === 0 
        || active_filters.type.includes(img_data.type);

        return rarity_match && type_match;
    });

    console.log(filtered_img_data);

    // 필터링된 데이터로 요소 생성
    createImgElement(filtered_img_data);
}

// 이미지 생성
function generateImg(IMG_GROUPS)
{
    // list_content 요소 제거
    document.getElementById("list_content").innerHTML = '';

    // 이중 for로 그룹 내 요소 하나하나 생성
    IMG_GROUPS.forEach(group => {
        // 그룹 컨테이너 생성
        const GROUP_CONTAINER = document.createElement("div");
        GROUP_CONTAINER.style.display = "inline-block";
        // 마진 값 설정
        GROUP_CONTAINER.style.marginRight = "40px";
    
        // 이미지 생성 및 컨테이너에 추가
        group.forEach(img_info => {
            // 요소 생성
            const IMG_ELEMENT = document.createElement("img");

            // 이미지 클릭 이벤트 추가
            IMG_ELEMENT.addEventListener("click", function() {
                // 상태 값 반전 
                img_info.status = !img_info.status;

                // 상태 값에 따라 비활성화 여부 결정
                if(img_info.status)
                    IMG_ELEMENT.classList.remove("deactive");
                else
                    IMG_ELEMENT.classList.add("deactive");
            });

            // 상태 값에 따라 비활성화 여부 결정
            if(img_info.status)
                IMG_ELEMENT.classList.remove("deactive");
            else
                IMG_ELEMENT.classList.add("deactive");

            // 이미지 url 설정
            IMG_ELEMENT.src = img_info.url;

            // 컨테이너에 추가
            GROUP_CONTAINER.appendChild(IMG_ELEMENT);
        });
        // list_content에 추가
        document.getElementById("list_content").appendChild(GROUP_CONTAINER);
    })
}

// 인접 리스트 생성
function createAdjList(REL_MAP)
{
    const ADJ_LIST = {};

    REL_MAP.forEach((to, from) =>
    {
        if(!ADJ_LIST[from])
            ADJ_LIST[from] = [];

        ADJ_LIST[from].push(to);
    });

    return ADJ_LIST;
}

// 이미지 그루핑용 dfs
function dfs(node, adj_list, visited, group)
{
    // 방문 true
    visited[node] = true;
    // 그룹에 추가
    group.push(node);
    
    if(adj_list[node])
    {
        adj_list[node].forEach(neighbour => {
            // 방문 안한게 있으면 재귀
            if(!visited[neighbour])
                dfs(neighbour, adj_list, visited, group);
        });
    }
}


// 이미지 그루핑
function imgGrouping(img_infos, rel_map)
{
    // 인접 리스트
    const ADJ_LIST = createAdjList(rel_map);

    // console.log(ADJ_LIST);
    // 방문 기록
    const VISITED = [];
    // 이미지 그룹
    const IMG_GROUPS = [];
    // 모든 이미지 ID
    const ALL_ID = img_infos.reduce((acc, img_info) => {
        acc[img_info.id] = img_info;

        return acc;
    }, {});

    img_infos.forEach(img_info => {
        // 미방문 id 일때
        if(!VISITED[img_info.id])
        {
            // 그룹 생성
            const group = [];
            // dfs 로 그룹 찾기
            dfs(img_info.id, ADJ_LIST, VISITED, group);
            IMG_GROUPS.push(group.map(id => ALL_ID[id]));
        }
    });

    return IMG_GROUPS;
}



// 이미지 간 관계 설정
// 기본은 [1] 말고 같은 숫자일때 관계가 있는데, 예외도 있음(4로 시작할때나 속성이 바뀌는 경우)
function buildImgRelation(img_infos)
{
    const RELATION_MAP = new Map();

    img_infos.forEach((img_info, index) => {
        if(index < img_infos.length - 1)
        {
            const cur_id = img_info.id;
            const next_id = img_infos[index + 1].id;

            // 두 번째 문자만 제외하고 비교
            // const cci = cur_id.substring(0, 1) + cur_id.substring(2);
            // const nni = next_id.substring(0, 1) + next_id.substring(2);

            const cci = cur_id.substring(2);
            const nni = next_id.substring(2);

            if (cci === nni) 
            {
                // 관계가 확인되면 Map에 추가합니다.
                RELATION_MAP.set(cur_id, next_id);
            }
        }
    });

    return RELATION_MAP;
}

// 이미지 정보 객체 이름과 속성 순 정렬
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

// 이미지명 가져오기
function getImgData()
{
    // github api로 이미지 디렉토리 접근
    return fetch('https://api.github.com/repos/junsarakill/GASM.github.io/contents/SKGS/raw_img?ref=SKGS_Rework', {
            Headers: {
                "Authorization" : "token SKGS"
            }})
        .then(response => response.json())
        .then(data => {
            // 이미지 이름,데이터를 담을 배열
            let img_data = [];

            data.forEach(file => {
                // @@ 나중에는 조건 달아서 필요한 이미지만 가져와야 할지도
                img_data.push({
                    name : file.name
                    ,url: file.download_url
                    ,rarity : file.name[6]
                    ,type : file.name[11]
                });
            });
            return img_data;
        })
        .catch(error => {
            console.error(error)
            return [];
        });
}

