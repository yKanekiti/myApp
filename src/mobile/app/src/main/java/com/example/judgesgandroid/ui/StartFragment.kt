package com.example.judgesgandroid.ui

import android.annotation.SuppressLint
import android.database.Cursor
import android.net.Uri
import android.os.Bundle
import android.provider.MediaStore
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.core.net.toFile
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.MutableLiveData
import com.example.judgesgandroid.R
import com.example.judgesgandroid.databinding.FragmentStartBinding
import com.example.judgesgandroid.entity.response.PredictResponse
import com.example.judgesgandroid.viewmodel.StartViewModel
import timber.log.Timber
import java.io.File

class StartFragment : Fragment() {

    lateinit var binding: FragmentStartBinding
    private val viewModel: StartViewModel by viewModels()
    lateinit var launcher: ActivityResultLauncher<String>

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentStartBinding.inflate(layoutInflater, container, false)
        /* 実機に保存されている content を mimeType 指定で取得するアプリの launcher */
        launcher = registerForActivityResult(ActivityResultContracts.GetContent()) { uri ->
            /* activity result を受け取った後に実行される処理 */

            /* 画像をビューにセットする */
            binding.imageView.setImageURI(uri)
            binding.judgeButton.isEnabled = true

            /* 画像情報をViewModelにセットする */
            viewModel.uriLiveData.value = uri

            /* 画像が変わったら以前の結果をクリアする */
            viewModel.resultLiveData.value = null
            binding.resultText.text = ""

        }
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {

        setupButtonClickListeners()
        setupLiveData()
    }

    /**
     * ボタンクリックリスナを登録する
     */
    private fun setupButtonClickListeners() {
        /* 画像選択ボタン */
        binding.imageSelectButton.setOnClickListener {
            /* launcher を起動する(実機に保存されている content を mimeType 指定で取得するアプリを立ち上げる) */
            launcher.launch("image/*")
        }

        /* 判定ボタン */
        binding.judgeButton.setOnClickListener {
            context?.let {
                viewModel.predict(it)
            }
        }
    }

    @SuppressLint("SetTextI18n")
    private fun setupLiveData() {
        viewModel.resultLiveData.observe(viewLifecycleOwner, { res ->
            /* 結果を受け取った後 */
            res?.resultList?.find { it.id == res.maxId }?.let {
                /* 結果を表示 */
                binding.resultText.text = "たぶん${it.name}やんなこれ知ってるで"

                /* 葉ノードの場合は判定ボタンを非活性にする */
                if (it.isLeaf != 0) {
                    binding.judgeButton.isEnabled = false
                }
            }
        })
    }
}

