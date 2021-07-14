package com.example.judgesgandroid.entity.models

import com.squareup.moshi.Json

/**
 * 判定結果
 * @property id     ノードのID
 * @property name   ノードの名前
 * @property value  結果値
 * @property isLeaf ノードが葉かどうか(0以外なら葉)
 */
data class Result(
    val id: Int,
    val name: String,
    val value: Float,
    @Json(name = "is_leaf") val isLeaf: Int
)
