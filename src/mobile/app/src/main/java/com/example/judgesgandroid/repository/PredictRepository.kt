package com.example.judgesgandroid.repository

import android.content.Context
import android.database.Cursor
import android.net.Uri
import android.provider.MediaStore
import com.example.judgesgandroid.entity.request.PredictRequest
import com.example.judgesgandroid.entity.response.PredictResponse
import com.example.judgesgandroid.service.ServiceApi
import okhttp3.MediaType
import okhttp3.MultipartBody
import okhttp3.RequestBody
import retrofit2.Response
import java.io.File

class PredictRepository {
    private val service = ServiceApi.getApi()

    suspend fun predict(id: Int, uri: Uri, context: Context): Response<PredictResponse> {
        val map: MutableMap<String, RequestBody> = HashMap()
        val file: File = File(toFile(uri, context))
        val name: String = file.nameWithoutExtension
        map["id"] = RequestBody.create(MediaType.parse("text/plane"), id.toString())
        map["name"] = RequestBody.create(MediaType.parse("text/plane"), name)
        map["image\"; filename=\"$name.png\""] =
            RequestBody.create(MediaType.parse("image/png"), file)
        return service.judgeImage(map)
    }


    /**
     * UriをFileに変換する
     * @param uri 変換したいUri
     * @return 変換されたFileのパス
     */
    private fun toFile(uri: Uri, context: Context): String {
        /* 正直何してるか分からん */
        val cursor: Cursor = context?.contentResolver?.query(
            uri,
            arrayOf(MediaStore.Images.ImageColumns.DATA),
            null,
            null,
            null
        ) ?: return ""
        cursor.moveToFirst()
        val filePath = cursor.getString(0)
        cursor.close()
        return filePath
    }
}