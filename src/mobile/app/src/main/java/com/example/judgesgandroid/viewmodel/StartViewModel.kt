package com.example.judgesgandroid.viewmodel

import android.content.Context
import android.net.Uri
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.judgesgandroid.entity.request.PredictRequest
import com.example.judgesgandroid.entity.response.PredictResponse
import com.example.judgesgandroid.repository.PredictRepository
import kotlinx.coroutines.launch
import timber.log.Timber
import java.io.File

class StartViewModel : ViewModel() {

    private val repository = PredictRepository()
    var resultLiveData: MutableLiveData<PredictResponse> = MutableLiveData()
    val uriLiveData: MutableLiveData<Uri> = MutableLiveData()

    /**
     * 画像を判定する
     * @param file 画像ファイル
     */
    fun predict(context: Context) {
        uriLiveData.value?.let { uri ->
            viewModelScope.launch {
                /* maxIdは初回のみ1となる */
                val maxId: Int = resultLiveData.value?.maxId ?: 1
                val result = repository.predict(maxId, uri, context)

                Timber.d("result: $result")
                result.body()?.let {
                    resultLiveData.postValue(it)
                }
            }
        }
    }
}
