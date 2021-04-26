from ..enum.KindEnum import KindEnum


class Points:
    KINDS = {
        KindEnum.person: 4,
        KindEnum.hero: 5,
        KindEnum.fighter: 7,
        KindEnum.champion: 10,
        KindEnum.legend: 12
    }


class Messages:
    SUCCESS = "Success"
    FAIL = "Fail"
    MISSING_FIELD_KIND = 'Kind field cannot be null'
