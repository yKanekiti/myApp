package com.example.judgesgandroid.entity.response

import com.example.judgesgandroid.entity.models.Result
import com.squareup.moshi.Json

/**
 * 判定結果レスポンス
 * @property maxId          一番値の高いID
 * @property resultList     結果リスト
 */
data class PredictResponse(
    @Json(name = "max_id") val maxId: Int,
    @Json(name = "result_list") val resultList: List<Result>
)
