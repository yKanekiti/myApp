package com.example.judgesgandroid.service

import com.example.judgesgandroid.entity.response.PredictResponse
import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import okhttp3.MultipartBody
import okhttp3.RequestBody
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.http.Multipart
import retrofit2.http.POST
import retrofit2.http.Part
import retrofit2.converter.moshi.MoshiConverterFactory
import retrofit2.http.PartMap

interface ServiceApi {

    companion object {
        /* APIサーバー */
        private const val baseURL = "http://10.0.2.2:5000"

        /* おまじない */
        fun getApi(): ServiceApi {
            val moshi = Moshi.Builder()
                .add(KotlinJsonAdapterFactory())
                .build()
            return Retrofit.Builder()
                .baseUrl(baseURL)
                .addConverterFactory(MoshiConverterFactory.create(moshi))
                .build().create(ServiceApi::class.java)
        }
    }

    /**
     * 画像を判定する
     * @param params {id: ノードID, name: 画像名, image: 画像ファイル }
     * @return 判定結果
     */
    @JvmSuppressWildcards
    @Multipart
    @POST("/predict")
    suspend fun judgeImage(
        @PartMap params: Map<String, RequestBody>
    ): Response<PredictResponse>
}