// 이미지 번호 분석하기
// 캐릭터별 폴더 생성 후 이미지 이동
// cmn_mn 이미지 타입 : 256 아이콘 이미지

// 레어리티
const RARITY_MAP = new Map(
    [
        [0, "n"]
        ,[1, "r"]
        ,[2, "sr"]
        ,[3, "ssr"]
        ,[4, "ur"]
        ,[5, "lr"]
    ]
);
// 속성
const TYPE_MAP = new Map(
    [
        [0, "blue"]
        ,[1, "red"]
        ,[2, "yellow"]
        ,[3, "purple"]
        ,[4, "green"]
    ]
)
// 캐릭터 번호 맵 만들려 했는데 굳이 필요 없나?

// 이미지 정보
class imgInfo
{
    /* 이미지 이름을 받아서 정보 파싱
       전문 예시: cmn_cx10000200
       8자리 숫자
       [0] : 레어도 - 1:n 2:r 3:sr 4:ssr 5:ur 6:lr
       [1] : 각성여부 - 0:통상 1:통상(특수) 2:각성 3: 신유제(변신)
       [2:4] : 캐릭터번호 - ex 000(아스카) 165(손권) 비어있는 번호 있음
       [5] : 속성 - 0:blue 1:red 2:yellow 3:purple 4:green
       [6:7] : 출시 순서 - 00~99 속성이 같을 시 출시 순에 따라 00,01,02 순으로 지어짐
     */
    constructor(img_name = "cmn_cx87654321")
    {
        // 전문 6번째부터 끝까지가 id
        this.id = img_name.substring(6);
        // id 0 번째 레어도
        this.rarity = this.id[0];
        // 이름 번호
        this.name = this.id.substring(2,4);
        // 타입
        this.type = this.id[5];
        // 활성여부
        this.status = true;
    }
    
    // rarity 계산
    setRarity(rarity)
    {
        const RARITY_VALUE = RARITY_MAP.get(rarity);
        if(RARITY_VALUE != undefined)
            return RARITY_VALUE;
        else
        {
            console.log(`ID ${id}에 해당하는 레어리티가 없음`);
            return "unknown";
        }
    }
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
            const cci = cur_id.substring(0, 1) + cur_id.substring(2);
            const nni = next_id.substring(0, 1) + next_id.substring(2);

            if (cci === nni) 
                // 관계가 확인되면 Map에 추가합니다.
                RELATION_MAP.set(cur_id, next_id);
        }
    });

    return RELATION_MAP;
}

// 이미지명 비동기 가져오기
async function aGetImgInfos()
{
    const img_infos = await getImgNames();

    console.log(img_infos);
}

// 이미지명 가져오기
function getImgNames()
{
    // github api로 이미지 디렉토리 접근
    return fetch('https://api.github.com/repos/junsarakill/GASM.github.io/contents/SKGS/raw_img?ref=SKGS_Rework', {
            headers: {
                "Authorization" : "token SKGS"
            }})
        .then(response => response.json())
        .then(data => {
            let img_infos = [];

            data.forEach(file => {
                // 파일을 읽어서 이미지로 출력
                // const imgElement = document.createElement("img");
                // imgElement.src = file.download_url;
                // document.getElementById("list_content").appendChild(imgElement);

                // 이미지명 가져오기
                img_infos.push(file.name);
            });
            return img_infos;
        })
        .catch(error => {
            console.error(error)
            return [];
        });
}

