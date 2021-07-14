package com.example.judgesgandroid.entity.request

import java.io.File


data class PredictRequest(
    val id: Int,
    val name: String,
    val file: File
)
