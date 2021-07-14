package com.example.judgesgandroid.ui

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.navigation.fragment.findNavController
import com.example.judgesgandroid.R
import com.example.judgesgandroid.databinding.FragmentTopBinding

class TopFragment : Fragment() {

    lateinit var binding: FragmentTopBinding

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        binding = FragmentTopBinding.inflate(layoutInflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        binding.constraintLayoutTop.setOnClickListener {
            findNavController().navigate(R.id.action_TopFragment_to_startFragment)
        }
    }
}